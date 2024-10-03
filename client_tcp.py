import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(2)


try:
    client.connect(("google.com", 4466))    #DEFINIÇÃO DO CLIENT E A PORTA QUE QUEREMOS EFETUAR A CONEXÃO:
    client.send(b"GET / HTTP/1.1\nHost: www.google.com\n\n\n")  #REQUISICAO DA PAGINA EX: GET / HTTP/2 ou 1.1\nHost: www.google.com
    received_packets = client.recv(1024).decode()
    print(received_packets)  
except Exception as error:
    print(">>>>> An error has occurred. <<<<<")
    print(error)
