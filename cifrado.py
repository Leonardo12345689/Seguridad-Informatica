from cryptography.fernet import Fernet



def cargar_clave():
    return open("clave.key", "rb").read()


def genera_clave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)


def encriptar(nombreArchivo, clave):
    f = Fernet(clave)
    with open(nombreArchivo, "rb") as file:
        archivo_info = file.read()
    encrypted_data = f.encrypt(archivo_info)
    with open(nombreArchivo, "wb") as file:
        file.write(encrypted_data)


genera_clave()

clave = cargar_clave()


nombreArchivo = "text.txt"
encriptar(nombreArchivo, clave)
