def solicitar_informacion_planta(): #Solicita la información inicial
    tipos_validos = ["flor", "árbol", "arbusto", "suculenta", "helecho"] #tipos de planta aceptados
    input("¡Bienvenido a Verde Vida! \nPresiona enter para continuar")
    while True:

        tipo_planta = input("Introduce el tipo de planta (flor, árbol, arbusto, suculenta, helecho): ").lower() #lectura de planta
        if tipo_planta in tipos_validos:
            break
        else:
            print("Tipo de planta no válido. Por favor, introduce uno de los siguientes: flor, árbol, arbusto, suculenta, helecho.") #validación de error de planta

    nombre_planta = input("Introduce el nombre de la planta: ") #guarda nombre de planta

    while True:
        try:
            nivel_agua = float(input("Introduce el nivel inicial de agua (número): ")) #solicitud de nivel de agua
            if nivel_agua < 0:
                print("El nivel de agua no puede ser negativo. Por favor, introduce un número válido.") #si es menor a cero no se acepta
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.") #validacion de numeros

    while True:
        try:
            nivel_nutrientes = float(input("Introduce el nivel inicial de nutrientes en la tierra (número): ")) #solicitud de nutrientes
            if nivel_nutrientes < 0:
                print("El nivel de nutrientes no puede ser negativo. Por favor, introduce un número válido.")#si es menor a cero no se acepta
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.") #validacion de numeros
    
    #declaración de variables en planta
    planta = {
        "tipo": tipo_planta,
        "nombre": nombre_planta,
        "nivel_agua": nivel_agua,
        "nivel_nutrientes": nivel_nutrientes,
        "nivel_sol": 0,
        "veces_regada": 0
    }

    return planta

def mostrar_menu(): #muestra el menú de opciones
    print("\nMenú de opciones:")
    print("1. Ver información de planta")
    print("2. Regar planta")
    print("3. Asolear planta")
    print("4. Abonar planta")
    print("5. Simular paso del tiempo")
    print("6. Salir")

def ver_informacion_planta(planta): #opción 1, muestra la información guardada actualmente
    print("\nInformación de la planta:")
    print(f"Tipo: {planta['tipo']}")
    print(f"Nombre: {planta['nombre']}")
    print(f"Nivel de agua: {planta['nivel_agua']:.2f}")
    print(f"Nivel de nutrientes: {planta['nivel_nutrientes']:.2f}")
    print(f"Nivel de sol: {planta['nivel_sol']:.2f}")

def regar_planta(planta): #Riega planta, opción 2
    if planta['veces_regada'] < 5: #si es menor a 5 permite realizar el riego
        if planta['nivel_agua'] == 0: # se valida si es mayor a cero para evitar operar porcentaje en cero
            planta['nivel_agua'] += 1  # Incremento mínimo si el nivel de agua es 0
        else:
            incremento = planta['nivel_agua'] * 0.07 #aumento del 7%
            planta['nivel_agua'] += incremento
        planta['veces_regada'] += 1 #aumenta contador de veces regado
        print(f"\nHas regado la planta. Nuevo nivel de agua: {planta['nivel_agua']:.2f}")
    else:
        print("\nLa planta ya ha sido regada el máximo de 5 veces. No se puede regar más.")

def asolear_planta(planta): #opción 3 asolear
    decremento = planta['nivel_agua'] * 0.05 #Se obtiene el 5%
    if planta['nivel_agua'] > decremento: #Si la cantidad de agua es mayor al decremento, se puede operar
        planta['nivel_agua'] -= decremento #se resta el decremente obtenido previamente
        planta['nivel_sol'] += 1 #aumenta el nivel de sol
        print(f"\nHas expuesto la planta al sol. Nuevo nivel de agua: {planta['nivel_agua']:.2f}")
    else:
        print(f"\nNo es recomendable asolear la planta. Nivel de agua actual: {planta['nivel_agua']:.2f}") #Si el agua es menor al decremento no permite realizar la operacion porque la planta muere

def abonar_planta(planta): #opción 4,abono
    if planta['nivel_nutrientes'] < 500: #Si es menor a 500 permite realizar operación
        if planta['nivel_nutrientes'] > 0:  # Asegurarse de que los nutrientes sean positivos
            planta['nivel_nutrientes'] *= 2
        else:
            planta['nivel_nutrientes'] += 50  # Incremento en 50 si el nivel de nutrientes es 0
        print(f"\nHas abonado la planta. Nuevo nivel de nutrientes: {planta['nivel_nutrientes']:.2f}")
    else:
        print(f"\nEl nivel de nutrientes es demasiado alto para abonar. Nivel de nutrientes actual: {planta['nivel_nutrientes']:.2f}") #si es mayor a 500 se indica que no se puede realizar

def simular_paso_del_tiempo(planta): #opción 5, simular tiempo
    while True:
        try:
            horas = int(input("¿Cuántas horas deseas simular?: ")) #solicitud de horas de simulación
            if horas < 0:
                print("El número de horas no puede ser negativo. Por favor, introduce un número válido.") #validación de numeros positivos
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

    nivel_agua_inicial = planta['nivel_agua'] #se obtiene nivel de agua en variable local
    nivel_nutrientes_inicial = planta['nivel_nutrientes'] #se obtiene nutrientes en variable local
 
    for _ in range(horas): #recorre hasta finaliar cantidad de horas
        planta['nivel_agua'] -= planta['nivel_agua'] * 0.05 #se resta 5% por cantidad de horas
        planta['nivel_nutrientes'] -= 50
        if planta['nivel_nutrientes'] < 0: #si nutrientes llega a ser negativo se coloca como cero
            planta['nivel_nutrientes'] = 0

    total_disminucion_agua = nivel_agua_inicial - planta['nivel_agua'] #muestra disminucion de agua
    total_disminucion_nutrientes = nivel_nutrientes_inicial - planta['nivel_nutrientes'] #muestra disminucion de nutrientes

    print("\nHa pasado el tiempo.")
    print(f"El nivel de agua disminuyó en un {total_disminucion_agua / nivel_agua_inicial * 100:.2f}%.")
    print(f"El nivel de nutrientes se redujo en un total de {total_disminucion_nutrientes:.2f} unidades.")
    print(f"Nuevos niveles - Agua: {planta['nivel_agua']:.2f}, Nutrientes: {planta['nivel_nutrientes']:.2f}")

def main(): #main donde se llaman las funciones para realizar cada proceso
    planta = solicitar_informacion_planta()
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            ver_informacion_planta(planta)
        elif opcion == '2':
            regar_planta(planta)
        elif opcion == '3':
            asolear_planta(planta)
        elif opcion == '4':
            abonar_planta(planta)
        elif opcion == '5':
            simular_paso_del_tiempo(planta)
        elif opcion == '6':
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
