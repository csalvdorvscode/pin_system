Python 3.13.12 (v3.13.12:1cbe4818347, Feb  3 2026, 13:36:53) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> 
>>> #SISTEMA DE PIN:
>>> 
>>> pin_correcto=1234
>>> intentos=0
>>> 
>>> while intentos<3:
...     pin_usuario= int(input("Introduce la contraseña"))
...     if pin_usuario == pin_correcto:
...         print("Pin correcto")
...         break
...     else:
...         print("Pin incorrecto")
...         intentos +=1
...         print("te queda", 3-intentos,"intentos")
...     if intentos == 3:
...         print("Cuenta bloqueada")
... 
...         
Introduce la contraseña 12234
Pin incorrecto
te queda 2 intentos
Introduce la contraseña 232454
Pin incorrecto
te queda 1 intentos
Introduce la contraseña123444
Pin incorrecto
te queda 0 intentos
Cuenta bloqueada
