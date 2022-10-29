import socket



B_priv = str(input('Ingrese clave privada del Servidor:\n'))


def server(B_priv):
    host = "127.0.0.1" #Asignar ip
    port = 1234 #Asignar puerto

    server_socket = socket.socket()  #Obtener la instancia
    server_socket.bind((host, port))  #junta la ip con el puerto

    server_socket.listen(1) #Definir cuantos clientes pudo tener conectados
    conn, address = server_socket.accept()  #Para aceptar nuevas conexiones
    print("Connection from: " + str(address))

    #Recivir P
    P = int(conn.recv(1024).decode())
    if not P:
            #si no se recive el paquete, se corta la conexion
            conn.close()
    print("P es: " + str(P))

    #Enviar temp
    temp=0
    conn.send(str(temp).encode())  #envio de paquete a cliente


    #Recivir Q
    Q = int(conn.recv(1024).decode())
    if not Q:
            #si no se recive el paquete, se corta la conexion
            conn.close()
    print("Q es: " + str(Q))


    #Calculo clave publica servidor
    B_pub= P**int(B_priv)%Q

    #Enviar B_Pub
    conn.send(str(B_pub).encode())  #envio de paquete a cliente

    #Recivir A_Pub
    A_pub = conn.recv(1024).decode()
    if not A_pub:
            #si no se recive el paquete, se corta la conexion
            conn.close()
    print("La clave publica del Cliente es: " + str(A_pub))

    #Calculo llave sincronizada
    K_B= int(A_pub)**int(B_priv)%int(Q)

    #Enviar llave sincronizada por parte del servidor
    conn.send(str(K_B).encode())  #envio de paquete a cliente


    #Recivir K_A
    K_A = conn.recv(1024).decode()
    if not K_A:
            #si no se recive el paquete, se corta la conexion
            conn.close()
    print("La llave sincronizada por parte del cliente es: " + str(K_A))


    if K_A == str(K_B):
        print('Las llaves están sincronizadas!')
    else:
        print('Las llaves no están sincronizadas :((')

    conn.close()  #Termino de conexion




if __name__ == '__main__':
    server(B_priv)






