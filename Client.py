import socket





Q = str(input('Ingrese un numero primo:\n'))
i = True
while i == True:
    P = str(input('Ingrese un numero menor al anterior, pero mayor a 0:\n'))
    if int(P) < int(Q) and int(P) > 0:
        i = False
    else:
        i = True
A_priv = str(input('Ingrese clave privada del Clienteeeeeeeee:\n'))









def client(P,Q,A_priv):
    host = "127.0.0.1"
    port = 1234

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    #enviar P
    client_socket.send(str(P).encode())

    #Recivir temp
    temp = int(client_socket.recv(1024).decode())

    #enviar Q
    client_socket.send(str(Q).encode())

    #Recivir B_pub
    B_pub = client_socket.recv(1024).decode()
    print("La clave publica del servidor es: " + str(B_pub))


    #Calculo clave publica servidor
    A_pub= int(P)**int(A_priv)%int(Q)



    #enviar A_pub
    client_socket.send(str(A_pub).encode())


    #Recivir llave sincronizada del servidor
    K_B = client_socket.recv(1024).decode()
    print("La llave sincronizada del servidor es: " + str(K_B))

    K_A= int(B_pub)**int(A_priv)%int(Q)

    #Enviar llave sincronizada por parte del cliente
    client_socket.send(str(K_A).encode())

    if K_A == int(K_B):
        print('Las llaves están sincronizadas!')
    else:
        print('Las llaves no están sincronizadas :((')



    client_socket.close()  # close the connection


if __name__ == '__main__':
    client(P,Q,A_priv)

