# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 1. Criamos as ferramentas vazias
db = SQLAlchemy()
app = Flask(__name__)

# 2. Configuração: Onde vai ficar o arquivo do banco?
# Vamos chamar de 'doce_flautas.db' para ficar temático!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doce_flautas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Ligamos o banco ao app
db.init_app(app)

# 4. Importamos os modelos para o SQLAlchemy conhecê-los
# (O Python vai ler o arquivo models.py nesse momento)
from . import models
from . import routes