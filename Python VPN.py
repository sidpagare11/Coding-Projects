import socket
import threading


# proxy serving initialization
proxy_host = '127.0,01'
proxy_port = 8888



# destination for server intialization
destination_host = 'google.com'
destination_port = 80



def handle_client(clinet_socket):
    # connect to destination server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((destination_host, destination_port))



# transfer data between client and server
    while True:
        client_data = clinet_socket.recv(4096)
        if len(client_data) == 0:
            break

        # send data to the server
        server_socket.send(client_data)

    #close the connection
    clinet_socket.close()
    server_socket.clsoe()



def start_proxy():
# create socket object
    proxy = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# bind the socket to the host and port
    proxy.bind((proxy_host, proxy_port))


#listen for incoming connections
    proxy.listen(5)
    print(f'Proxy server is listening on {proxy_host}: {proxy_port}')


    while True:
        client_socket, addr = proxy.accept()
        print(f'Accepted the connection from {addr[0]}: {addr[1]}')

        # thread to handle the client
        clinet_handle = threading.Thread(target=handle_client, args=(client_socket,))
        clinet_handle.start()



if __name__ == '__main__':
    start_proxy()

