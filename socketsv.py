import socket 

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor_socket.bind(('localhost', 12345))
servidor_socket.listen()

print('[+] Servidor escuchando en localhost:12345')

cliente_socket, address = servidor_socket.accept()

print('[+] Conexión establecida con', address)

while True:
    data = cliente_socket.recv(1023)
    if not data:
        break
    print('[+] Mensaje recibido: ', data.decode())

    message = '[+] Mensaje enviado correctamenmte'.encode()
    cliente_socket.send(message)

cliente_socket.shutdown(socket.SHUT_RDWR)

cliente_socket.close()
servidor_socket.close()


