from senha import API_KEY
import requests
import json

def askGPT(tema, quantidade, autor):
    q_imagem = float(quantidade)/5
    pergunta = f"Monte uma apresentação sobre {tema} com {quantidade} slides, incluindo a capa e imagens ilustrativas. A capa é o Slide 0 deve conter o título e o autor {autor}. Cada slide deve seguir o padrão de identificação Slide: Título, Tópicos. Insira a palavra Imagem apenas nos tópicos de {q_imagem} slides."

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    id_modelo = "gpt-3.5-turbo"
    link = "https://api.openai.com/v1/chat/completions"

    body_message = {
    "model": id_modelo,
     "messages": [
         {"role": "user", "content": pergunta}
     ],
    }

    # Tranforma dicionário Python em Json
    body_message = json.dumps(body_message)
    
    requisicao = requests.post(link, headers=headers, data=body_message)
    print(requisicao)
    # print(requisicao.text)
    
    resposta = requisicao.json()
    # print(resposta)
    # print(resposta['choices'][0]['message']['content'])
    
    file = open("info_presentation.txt","w", encoding = "utf-8")
    file.write(resposta['choices'][0]['message']['content'])
    file.close()
    
    with open("info_presentation.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.readlines()
    
    texto.pop()
    # print(texto)