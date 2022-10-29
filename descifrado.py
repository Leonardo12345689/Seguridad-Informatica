from cryptography.fernet import Fernet


def cargar_clave():
    return open("clave.key","rb").read()


def desencriptar(nombreArchivo, clave):
    f = Fernet(clave)
    with open(nombreArchivo, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(nombreArchivo, "wb") as file:
        file.write(decrypted_data)

clave = cargar_clave()

nombre_archivo = "text.txt"

desencriptar(nombre_archivo, clave)
