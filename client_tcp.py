import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(2)


try:
    client.connect(("google.com", 4466))
    client.send(b"GET / HTTP/1.1\nHost: www.google.com\n\n\n")
    received_packets = client.recv(1024).decode()
    print(received_packets)  
except Exception as error:
    print(">>>>> An error has occurred. <<<<<")
    print(error)
