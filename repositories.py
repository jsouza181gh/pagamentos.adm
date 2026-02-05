from models import Fornecedor, Colaborador, session

def criarFornecedor(novoNome, novoCnpj, novoEmail, novaSenha):
    novoFornecedor = Fornecedor(
        nome=novoNome, 
        cnpj=novoCnpj,
        email=novoEmail, 
        senha=novaSenha
    )
    session.add(novoFornecedor)
    session.commit()

def criarColaborador(novoNome, novaMatricula, novoEmail, novaSenha):
    novoColaborador = Colaborador(
        nome=novoNome,
        matricula=novaMatricula,
        email=novoEmail,
        senha=novaSenha
    )
    session.add(novoColaborador)
    session.commit()

def buscarSenhaFornecedor(emailFornecedor):
    fornecedor = session.query(Fornecedor).filter_by(email=emailFornecedor).first()
    return fornecedor.senha

def buscarSenhaColaborador(emailColaborador):
    colaborador = session.query(Colaborador).filter_by(email=emailColaborador).first()
    return colaborador.senha

def editarFornecedor(idFornecedor, novoNome, novoCnpj, novoTelefone, novoEmail, novaSenha):
    fornecedor = session.query(Fornecedor).filter_by(id=idFornecedor).first()
    fornecedor.nome = novoNome
    fornecedor.cnpj = novoCnpj
    fornecedor.telefone = novoTelefone
    fornecedor.email = novoEmail
    fornecedor.senha = novaSenha
    session.add(fornecedor)
    session.commit()

def excluirFornecedor(idFornecedor):
    fornecedor = session.query(Fornecedor).filter_by(id=idFornecedor).first()
    session.delete(fornecedor)
    session.commit()