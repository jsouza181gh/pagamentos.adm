from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine('sqlite:///pagamentosADM.db')
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String(100), nullable=False)
    cnpj = Column('cnpj', String(20), nullable=False)
    email = Column('email', String(100), unique=True, nullable=False)
    senha = Column('senha', String(100), nullable=False)

    def __init__(self, nome, cnpj, email, senha):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.senha = senha

class Colaborador(Base):
    __tablename__ = 'colaboradores'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String(100), nullable=False)
    matricula = Column('matricula', String(100), nullable=False)
    email = Column('email', String(100), unique=True, nullable=False)
    senha = Column('senha', String(100), nullable=False)

    def __init__(self, nome, matricula, email, senha):
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.senha = senha

Base.metadata.create_all(db)