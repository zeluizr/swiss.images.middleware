import os
import json


def listar_imagens_e_criar_json(diretorio_imagens, url_base, arquivo_saida):
    # Lista para armazenar os dados de cada imagem
    dados_imagens = []

    # Listar arquivos no diretório especificado
    for arquivo in os.listdir(diretorio_imagens):
        if arquivo.endswith(
            (".png", ".jpg", ".jpeg")
        ):  # Verificar a extensão do arquivo para incluir apenas imagens
            nome_imagem = os.path.splitext(arquivo)[
                0
            ]  # Remover a extensão do arquivo para obter o nome
            is_main = nome_imagem.endswith("_1")  # Verificar se o nome termina com '_1'

            # Extrair o ID da imagem antes do primeiro '_'
            id_imagem = nome_imagem.split("_")[0]

            dados_imagens.append(
                {
                    "IsMain": is_main,
                    "Label": nome_imagem,
                    "Name": nome_imagem,
                    "Text": nome_imagem,
                    "Url": f"{url_base}/{arquivo}",
                    "Id": int(id_imagem),
                }
            )

    # Escrever os dados em um arquivo JSON
    with open(arquivo_saida, "w") as f:
        json.dump(dados_imagens, f, indent=4)


# Caminho para o diretório que contém as imagens
diretorio_imagens = "./images/commenteme"

# URL base onde as imagens são acessíveis via web
url_base = "https://swiss.up.railway.app/images"

# Nome do arquivo JSON de saída
arquivo_saida = "dados_imagens.json"

# Executar a função
listar_imagens_e_criar_json(diretorio_imagens, url_base, arquivo_saida)
