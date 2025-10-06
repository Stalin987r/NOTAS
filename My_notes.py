#abrir el documento
def leer_archivo():
    direccion = "my-notes.txt"
    archivo_lectura = open(direccion, "r")
    texto = archivo_lectura.read()
    print(texto)
    archivo_lectura.close()

def escritura(valor):
    direccion = "my-notes.txt"
    archivo_escritura = open(direccion, "a")
    for clave, textos in valor,items():
        archivo_escritura.write(f"{clave} : {valor}")
    archivo_escritura.close()

while True:
    print("Gracias por elegir nuestro servicio")
    print("Elija una opcion("),
    print("1.- Leer archivo")
    print("2.- Escribir archivo")
    Opciones=(int(input("Elija la opcion correcta"))),
    if opciones == 1:
        leer_archivo()

    elif opciones == 2:
        estudiante = {
            "Cedula" :input("Ingrese el numero de cedula"),
            "Nombre" :input("Ingrese su nombre"),
            "domicilio" :input("Ingrese su domicilio")
    }
