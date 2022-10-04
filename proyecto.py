# Sistema que nos permita hacer un ABM
# Practico 1: Creación de menus: Usar estructuras de datos
# Crear una calculadora

# El programa calcula ingresando valores de tipo entero, rechaza cualquier otro tipo de dato

# print("¿Que cálculo desea hacer?")

# print("""       
#             Calculadora

# 1) Suma
# 2) Resta
# 3) Multiplicación
# 4) División
# 5) Potencia
# 6) Salir
# """)

# op=input("Ingresar opción: ")
# while not op.isnumeric() or int(op)>6: #Bucle que no permite datos que no sean numéricos
#     op=input("Ingresar una opción válida: ")
# op=int(op)

# a=input("Ingresar primer número: ") 
# b=input("Ingresar segundo número: ")
# while not a.isnumeric() or not b.isnumeric(): #Bucle que no permite datos que no sean numéricos
#     a=input("Ingresar primer número por favor: ")
#     b=input("Ingresar segundo número por favor: ")
# a=int(a)
# b=int(b)

# if op == 1: #Uso el if como una condición entre las de la lista mostrada
#     suma=a+b
#     print(suma)
# elif op == 2:
#     resta=a-b
#     print(resta)
# elif op == 3:
#     multi=a*b
#     print(multi)
# elif op == 4:
#     if b == 0: #Uso este if para crear una "excepcion" y que no tire error en la division en caso de ser division por 0
#         print("No se puede dividir por 0. ")
#     else:
#         divi=a/b
#         print(divi)   
# elif op == 5:
#     pot=a**b
#     print(pot)
# else:
#     print("Usted ha salido exitosamente. ")

# --------------------------------------------------------------------------------------------------------------------------------------

def saludo(n):
    # Función la cual saluda, seguido de una variable
    print("Hola "+ n)
    return


