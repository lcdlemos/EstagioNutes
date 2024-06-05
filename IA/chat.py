from senha import API_KEY
import requests
import json

# def askGPT(tema, quantidade, autor):
def askGPT(tema, autor):
    pergunta = f"Como professor universitário, crie uma apresentação sobre {tema}. O slide 1 da apresentação deve ser a capa com o título {tema} e o nome do autor {autor}. O último slide deve ser a conclusão. Cada slide deve conter um rótulo identificando o título. Devem ser inseridas imagens nos casos que houver exemplos."

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