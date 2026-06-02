#SISTEMA DE PIN:
>>> 
>>> pin_correcto = 1234
intentos = 0
max_intentos = 3

print("SISTEMA DE PIN")

while intentos < max_intentos:
    try:
        pin_usuario = int(input("Introduce el PIN: "))

        if pin_usuario == pin_correcto:
            print("PIN correcto. Acceso permitido.")
            break
        else:
            intentos += 1
            print(f"PIN incorrecto ({intentos}/{max_intentos})")

    except ValueError:
        intentos += 1
        print(f"Entrada no válida ({intentos}/{max_intentos})")

if intentos == max_intentos:
    print("Cuenta bloqueada")
