from models import Fornecedor, Colaborador, session

def criarFornecedor(novoNome, novoCnpj,novoTelefone, novoEmail, novaSenha):
    novoFornecedor = Fornecedor(
        nome=novoNome, 
        cnpj=novoCnpj,
        telefone=novoTelefone, 
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

def buscarFornecedor(idFornecedor=None, emailFornecedor=None):
    if not idFornecedor == None:
        fornecedor = session.query(Fornecedor).filter_by(id=idFornecedor).first()
        return {'Nome':fornecedor.nome,
                'CNPJ': fornecedor.cnpj,
                'Telefone': fornecedor.telefone,
                'E-mail': fornecedor.email,
                }
    elif not emailFornecedor == None:
        fornecedor = session.query(Fornecedor).filter_by(email=emailFornecedor).first()
        return fornecedor.senha

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

def exibirFornecedores():
    fornecedores = session.query(Fornecedor).all()
    tabelaFornecedores = {
    'id': [],
    'nome': [],
    'cnpj': [],
    'telefone': [],
    'email': [],
    'senha': [],
    }
    for fornecedor in fornecedores:
        tabelaFornecedores['id'].append(fornecedor.id)
        tabelaFornecedores['nome'].append(fornecedor.nome)
        tabelaFornecedores['cnpj'].append(fornecedor.cnpj)
        tabelaFornecedores['telefone'].append(fornecedor.telefone)
        tabelaFornecedores['email'].append(fornecedor.email)
        tabelaFornecedores['senha'].append(fornecedor.senha)
    
    return tabelaFornecedores

def exibirColaboradores():
    fornecedores = session.query(Colaborador).all()
    tabelaFornecedores = {
    'id': [],
    'nome': [],
    'matricula': [],
    'email': [],
    'senha': [],
    }
    for fornecedor in fornecedores:
        tabelaFornecedores['id'].append(fornecedor.id)
        tabelaFornecedores['nome'].append(fornecedor.nome)
        tabelaFornecedores['matricula'].append(fornecedor.matricula)
        tabelaFornecedores['email'].append(fornecedor.email)
        tabelaFornecedores['senha'].append(fornecedor.senha)
    
    return tabelaFornecedores

#criarFornecedor('João Emanuel Souza Rodrigues', '02.336.124/0014-92', '21979405435', 'joao.rodrigues@global.komatsu', '$2b$10$UxYdc6DBeD4gn3zPSEcFnOkzsaZxeQxWF4KAvc1FCszxRocojPRXu')
#print(buscarFornecedor(idFornecedor=2))
#editarFornecedor(2,'João Emanuel Souza Rodrigues', '02.336.124/0014-92', 'joao.rodrigues@global.komatsu', 'qwertyje123')
#excluirFornecedor(3)