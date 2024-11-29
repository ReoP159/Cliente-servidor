import socket
import threading

message_list = []

def handle_client(conn, addr):
    host,port = addr
    print(f'Se conectó un cliente en el puerto {port}')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        command = data.decode()
        if command.startswith('LAST'):
            # Process LAST request
            response = ""
            if(len(command)>12):
                response = handle_last_messages_request(command[5:])
            else:
                response = handle_last_messages_request('')
            print("Me pidieron:",response)
            conn.sendall(response.encode())
        else:
            print(f'Recibí de {port}:', command)
            message_list.append(command)
            conn.sendall(data)


def handle_get_request(command_data):
    # Replace this with your actual logic to handle GET requests
    return f"Pediste: {command_data}"

def handle_last_messages_request(command_data):
   cant = 3
   if(command_data!=""):
       cant = int(command_data)
   
   return  "".join([(m+'\n') for m in message_list[-cant:]])
    

def server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'El servidor comenzó a escuchas conexiones en el puerto {port}', (host, port))
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == '__main__':
    server()
