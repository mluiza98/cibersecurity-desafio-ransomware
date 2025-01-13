from cryptography.fernet import Fernet

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

def carregar_chave():
    return open("chave.key", "rb").read()

def criptografar_arquivo(arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)
    
    with open(arquivo, "rb") as arquivo_original:
        arquivo_bytes = arquivo_original.read()

    arquivo_criptografado = fernet.encrypt(arquivo_bytes)

    with open(arquivo + ".enc", "wb") as arquivo_criptografado_final:
        arquivo_criptografado_final.write(arquivo_criptografado)
    print(f"Arquivo {arquivo} criptografado com sucesso!")

gerar_chave()

arquivo = "teste.txt"  
criptografar_arquivo(arquivo)

