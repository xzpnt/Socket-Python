import socket 

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor_address = ('localhost', 12345)
cliente_socket.connect(servidor_address)

print('[+] Conexión establecida con', servidor_address)

while True:
    message = input('[+] Mensaje a enviar:')
    cliente_socket.send(message.encode())
    
    data = cliente_socket.recv(1023)


    print('[+] Respuesta recibida: ', data.decode())

    if message == 'exit':
        break

cliente_socket.shutdown(socket.SHUT_RDWR)

cliente_socket.close()