import csv
import io
from flask import Response, request, render_template
from datetime import datetime
# Importamos render_template para mostrar o HTML
from flask import request, render_template
from . import app, db
from .models import Aluno
from .models import Aluno, Ensaio, Chamada # Adicione Chamada aqui!

# NOVA ROTA: Só para MOSTRAR o formulário (GET)
@app.route("/matricula", methods=["GET"])
def abrir_formulario():
    return render_template("cadastro_aluno.html")

# ROTA ATUALIZADA: Agora aceita dados do Formulário HTML
@app.route("/alunos", methods=["POST"])
def criar_aluno():
    # Agora usamos request.form.get() porque vem do HTML
    # (Se viesse do Insomnia, seria request.json.get())
    dados = request.form 
    
    if 'nome' not in dados:
        return "Erro: Nome é obrigatório", 400
    
    novo_aluno = Aluno(
        nome=dados.get("nome"),
        curso=dados.get("curso"),
        tipo_flauta=dados.get("tipo_flauta"),
        telefone=dados.get("telefone"),
        deficiencia=dados.get("deficiencia")
    )
    
    db.session.add(novo_aluno)
    db.session.commit()
    
    # Em vez de devolver JSON, devolvemos uma mensagem simples na tela
    return "<h1>Sucesso! Aluno matriculado. 🎵</h1> <a href='/matricula'>Voltar</a>"
# app/routes.py

@app.route("/exportar")
def exportar_dados():
    # 1. Buscamos todos os alunos
    alunos = db.session.execute(db.select(Aluno)).scalars().all()

    # 2. Preparamos o arquivo na memória
    output = io.StringIO()
    
    # === CORREÇÃO 1: MUDAMOS O SEPARADOR PARA PONTO E VÍRGULA ===
    writer = csv.writer(output, delimiter=';')

    # 4. Escrevemos o Cabeçalho
    writer.writerow(['ID', 'Nome', 'Curso', 'Flauta', 'Telefone', 'Deficiência'])

    # 5. Escrevemos os dados
    for aluno in alunos:
        writer.writerow([
            aluno.id, 
            aluno.nome, 
            aluno.curso, 
            aluno.tipo_flauta, 
            aluno.telefone, 
            aluno.deficiencia
        ])

    # === CORREÇÃO 2: ADICIONAMOS O BOM (\ufeff) PARA OS ACENTOS ===
    return Response(
        '\ufeff' + output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=alunos_doce_de_flautas.csv"}
    )
# ===================================================================
# ROTAS DE ENSAIO
# ===================================================================

# ROTA GET: Mostrar o formulário
@app.route("/agendar_ensaio", methods=["GET"])
def abrir_agenda():
    return render_template("cadastro_ensaio.html")

# ROTA POST: Salvar o ensaio
@app.route("/ensaios", methods=["POST"])
def criar_ensaio():
    dados = request.form
    
    # Validação simples
    if not dados.get('data') or not dados.get('hora'):
        return "Erro: Data e Hora são obrigatórias", 400

    # === A MÁGICA DA CONVERSÃO ===
    # O HTML manda "2023-12-25" (String). O Banco quer Date.
    data_formatada = datetime.strptime(dados.get('data'), '%Y-%m-%d').date()
    
    # O HTML manda "14:30" (String). O Banco quer Time.
    hora_formatada = datetime.strptime(dados.get('hora'), '%H:%M').time()
    
    novo_ensaio = Ensaio(
        data=data_formatada,
        hora=hora_formatada,
        local=dados.get('local'),
        repertorio=dados.get('repertorio')
    )
    
    db.session.add(novo_ensaio)
    db.session.commit()
    
    return "<h1>Sucesso! Ensaio agendado. 📅</h1> <a href='/agendar_ensaio'>Agendar Outro</a>"
# app/routes.py

# ROTA GET: Mostrar a tela de chamada
@app.route("/chamada", methods=["GET"])
def abrir_chamada():
    # 1. Buscamos TODOS os ensaios (para preencher o select)
    lista_ensaios = db.session.execute(db.select(Ensaio)).scalars().all()
    
    # 2. Buscamos TODOS os alunos (para preencher os checkboxes)
    # Podemos ordenar por nome para ficar mais fácil achar!
    lista_alunos = db.session.execute(db.select(Aluno).order_by(Aluno.nome)).scalars().all()
    
    return render_template(
        "registrar_chamada.html", 
        ensaios=lista_ensaios, 
        alunos=lista_alunos
    )
# ROTA POST: Processar a chamada
@app.route("/chamada", methods=["POST"])
def salvar_chamada():
    # 1. Qual foi o ensaio escolhido?
    ensaio_id = request.form.get('ensaio_id')
    
    # 2. Quem veio? (Pega a LISTA de checkboxes marcados)
    # .getlist() é o segredo para pegar múltiplos valores com o mesmo nome!
    ids_presentes = request.form.getlist('alunos_presentes')
    
    # Validação básica
    if not ensaio_id:
        return "Erro: Selecione um ensaio!", 400

    # 3. Vamos salvar!
    # Primeiro, buscamos todos os alunos do banco para saber quem faltou também?
    # Por enquanto, vamos salvar APENAS QUEM VEIO como 'Presente=True'.
    # (Futuramente podemos salvar os faltosos como False se quisermos evoluir)
    
    for id_aluno in ids_presentes:
        nova_chamada = Chamada(
            ensaio_id=int(ensaio_id),
            aluno_id=int(id_aluno),
            presente=True
        )
        db.session.add(nova_chamada)
    
    db.session.commit()
    
    return f"<h1>Chamada realizada! ✅</h1><p>{len(ids_presentes)} alunos presentes registrados.</p><a href='/chamada'>Voltar</a>"