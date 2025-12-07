from . import db

# MODELO 1: ALUNO
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    # Aqui estava 'column' minusculo, corrigido para Column
    curso = db.Column(db.String(100), nullable=False)
    tipo_flauta = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    deficiencia = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "curso": self.curso,
            "tipo_flauta": self.tipo_flauta,
            "telefone": self.telefone,
            "deficiencia": self.deficiencia
        }

# MODELO 2: ENSAIO
class Ensaio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    local = db.Column(db.String(100), nullable=False)
    repertorio = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "data": str(self.data), # Convertendo data para texto
            "hora": str(self.hora), # Convertendo hora para texto
            "local": self.local,
            "repertorio": self.repertorio
        }

# MODELO 3: CHAMADA
class Chamada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    # Aqui estava 'nullabele', corrigido para nullable
    ensaio_id = db.Column(db.Integer, db.ForeignKey('ensaio.id'), nullable=False)
    # Aqui estava 'Bolean', corrigido para Boolean
    presente = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "aluno_id": self.aluno_id,
            "ensaio_id": self.ensaio_id,
            "presente": self.presente
        }
