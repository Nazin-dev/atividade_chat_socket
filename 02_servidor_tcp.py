import socket
from datetime import datetime

from protocolo_tcp import enviar_mensagem, receber_mensagem


HOST = "0.0.0.0"
PORTA = 9000


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

import socket

servidor = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

print("Objeto:", servidor)
print("Família:", servidor.family)
print("Tipo:", servidor.type)
print("Protocolo:", servidor.proto)
print("Descritor:", servidor.fileno())

servidor.bind((HOST, PORTA))
servidor.listen()


print("Endereço local:", servidor.getsockname())
print("Timeout:", servidor.gettimeout())
print(f"Servidor esperando em {HOST}:{PORTA}...")



conexao, endereco = servidor.accept()

print(f"Cliente conectado: {endereco}")


while True:

    mensagem = receber_mensagem(conexao)
    if mensagem is None:
        print("Cliente desconectou.")
        break

    if mensagem.startswith("/msg "):
        print("Cliente:", mensagem[5:])
        resposta = input("Resposta: ")
        enviar_mensagem(conexao, resposta)
    elif mensagem == "/hora":
        print("Cliente pediu o horário")
        enviar_mensagem(conexao, "Horário do servidor: " + datetime.now().strftime("%H:%M"))
    elif mensagem == "/sair":
        print("Cliente encerrou a conversa")
        enviar_mensagem(conexao, "Conversa encerrada.")
        break
    else:
        print("[ALERTA] Comando desconhecido:", mensagem)
        enviar_mensagem(conexao, "Comando desconhecido. Use /msg <texto>, /hora ou /sair")


conexao.close()
servidor.close()