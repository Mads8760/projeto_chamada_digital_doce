# run.py
from app import app, db

if __name__ == "__main__":
    # Contexto da aplicação para criar o banco
    with app.app_context():
        # A Mágica: "Crie todas as tabelas (Aluno, Ensaio, Chamada) agora!"
        db.create_all()
        print("Banco de dados 'doce_de_flautas.db' criado/verificado com sucesso!")

    # Liga o servidor
    app.run(debug=True)