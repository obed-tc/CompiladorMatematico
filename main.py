
import os
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSemantico import AnalizadorSemantico
from AnalizadorSintactico import AnalizadorSintactico

def procesar_linea(cadena_entrada):
    analizador_lexico = AnalizadorLexico(cadena_entrada)
    analizador_semantico = AnalizadorSemantico()
    analizador_sintactico = AnalizadorSintactico(analizador_lexico, analizador_semantico)
    try:
        resultado = analizador_sintactico.analizar()
        print(f"'{cadena_entrada}' = {resultado}")
    except Exception as e:
        print(f"Error '{cadena_entrada}' = {str(e)}")

def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                cadena_entrada = linea.strip()
                if cadena_entrada:
                    procesar_linea(cadena_entrada)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

def menu():
    os.system("cls")
    print("""\033[92m
 ::::::::   ::::::::  ::::    ::::  :::::::::  ::::::::::: :::            :::     :::::::::   ::::::::  :::::::::  
:+:    :+: :+:    :+: +:+:+: :+:+:+ :+:    :+:     :+:     :+:          :+: :+:   :+:    :+: :+:    :+: :+:    :+: 
+:+        +:+    +:+ +:+ +:+:+ +:+ +:+    +:+     +:+     +:+         +:+   +:+  +:+    +:+ +:+    +:+ +:+    +:+ 
+#+        +#+    +:+ +#+  +:+  +#+ +#++:++#+      +#+     +#+        +#++:++#++: +#+    +:+ +#+    +:+ +#++:++#:  
+#+        +#+    +#+ +#+       +#+ +#+            +#+     +#+        +#+     +#+ +#+    +#+ +#+    +#+ +#+    +#+ 
#+#    #+# #+#    #+# #+#       #+# #+#            #+#     #+#        #+#     #+# #+#    #+# #+#    #+# #+#    #+# 
 ########   ########  ###       ### ###        ########### ########## ###     ### #########   ########  ###    ### 

\033[0m          [\033[91m 1 \033[0m] Ejecutar linea
          [\033[91m 2 \033[0m] Seleccionar archivo
          [\033[91m 0 \033[0m] Salir
""")

def ejecutar_linea():
    print("\n===========================\n")
    cadena_entrada = str(input("Entrada\n>>> "))
    print("\nSalida \n")
    procesar_linea(cadena_entrada)
    print("\n===========================\n")
    input("Presione enter para continuar")

def ejecutar_archivo():
    nombre_archivo = input("Ingrese el nombre o ruta del archivo: ")
    os.system("cls")
    print("Archivo: " + nombre_archivo)
    print("\n======= Resultados ===========\n")
    procesar_archivo(nombre_archivo)
    print("\n===========================\n")
    input("Presione enter para continuar")

def validar_opcion(opcion):
    if opcion == "1":
        ejecutar_linea()
    elif opcion == "2":
        ejecutar_archivo()
    elif opcion == "0":
        exit()
    else:
        print("Opcion incorrecta")
        input("Presione enter para continuar")

def main():
    menu()
    opcion = str(input("\033[92m >>>  \033[0m"))
    validar_opcion(opcion)

if __name__ == "__main__":
    while True:
        main()
