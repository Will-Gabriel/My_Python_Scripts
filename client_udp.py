import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        msg = input("Menssage: ") + "\n"
        client.sendto(msg.encode(), ("127.0.0.1", 4433))    #1-BYTES À ENVIAR, 2-CONEXAO: HOST E PORTA
        data, sender = client.recvfrom(1024)
        print(f"{sender[0]}: {data.decode}")

        if data.decode() == "exit\n" or msg == "exit\n":
            break

    client.close()
except Exception as error:
    print(">>>>> An error has occurred. <<<<<")
    print(error)
    client.close()
