import socket

def client(host='127.0.0.1', port=65432):
    print(f'Conectando con el servidor en IP.{host}:{port}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            message = input('Mensaje: ')
            s.sendall(message.encode())
            if message.startswith('LAST'):
                data = s.recv(1024)
                print('recibí:', data.decode())

if __name__ == '__main__':
    client()
