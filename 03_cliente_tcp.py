import socket

from protocolo_tcp import enviar_mensagem, receber_mensagem


HOST = "IP_DO_SERVIDOR"
PORTA = 9000


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORTA))

print("Conectado ao servidor!")
print("Comandos: /msg <texto> | /hora | /sair")


while True:
    print("\n===== Nova conversa ====== \n")
    mensagem = input("Mensagem: ")

    enviar_mensagem(cliente, mensagem)

    resposta = receber_mensagem(cliente)

    if resposta is None:
        print("Servidor desconectou.")
        break

    print("Resposta Servidor:", resposta)

    print("\n========================= \n")

    if mensagem == "/sair":
        break

cliente.close()
