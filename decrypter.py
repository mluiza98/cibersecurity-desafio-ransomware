# decrypter.py
from cryptography.fernet import Fernet

# Função para carregar a chave de criptografia
def carregar_chave():
    return open("chave.key", "rb").read()

# Função para descriptografar um arquivo
def descriptografar_arquivo(arquivo_criptografado):
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(arquivo_criptografado, "rb") as arquivo_bytes:
        arquivo_criptografado_bytes = arquivo_bytes.read()

    arquivo_descriptografado = fernet.decrypt(arquivo_criptografado_bytes)

    # Remover a extensão .enc do nome do arquivo
    arquivo_original = arquivo_criptografado.replace(".enc", "")

    with open(arquivo_original, "wb") as arquivo_descriptografado_final:
        arquivo_descriptografado_final.write(arquivo_descriptografado)
    print(f"Arquivo {arquivo_criptografado} descriptografado com sucesso!")

# Descriptografar o arquivo teste.txt.enc
arquivo_criptografado = "teste.txt.enc"  # Nome do arquivo criptografado
descriptografar_arquivo(arquivo_criptografado)
