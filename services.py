from bcrypt import gensalt, hashpw, checkpw
from repositories import criarColaborador, criarFornecedor, buscarSenhaFornecedor, buscarSenhaColaborador

#Criar todos os "else", para erros aparecerem no HTML

def validarCadastro(chaveColaboradorLigada, nome, cnpjMatricula, email, senha, confirmacaoSenha):
    if senha == confirmacaoSenha:
        #Criar outras validações de senha
        senhaCriptografada = criptografarSenha(senha)
        if chaveColaboradorLigada:
            #Criar validação do CNPJ
            criarColaborador(
                nome,
                cnpjMatricula,
                email,
                senhaCriptografada
            )
        else:
            #Criar validação da matrícula
            criarFornecedor(
                nome,
                cnpjMatricula,
                email,
                senhaCriptografada
            )
        return True

def criptografarSenha(senha):
    salt = gensalt(rounds=10)
    novaSenha = senha.encode("utf-8")
    novaSenha = hashpw(novaSenha, salt)
    novaSenha = novaSenha.decode("utf-8")
    return novaSenha

def validarLogin(email, senha):
    #Criar função emailCadastrado() no repositories para validar se o email está cadastrado no banco
    try:
        hashSenha = buscarSenhaFornecedor(email)
    except:
        hashSenha = buscarSenhaColaborador(email)
    if checkpw(senha.encode('utf-8'), hashSenha.encode('utf-8')):
        return True