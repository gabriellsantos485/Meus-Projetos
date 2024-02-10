from openai import OpenAI
client = OpenAI(
    api_key= "sk*************************"
)



def enviar_mensagem(mensagem, lista_de_mensagem=[]):
    lista_de_mensagem.append(
        {'role': 'user', 'content': mensagem},
    )
    chat_completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = lista_de_mensagem,
    )
    return chat_completion #["choices"][0]["message"],

lista_de_mensagem = []
while True:
    texto = input("escreva sua mensagem")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_de_mensagem)
        lista_de_mensagem.append(resposta)
        print("chatbot", resposta)
