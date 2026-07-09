


planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],

}


inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15],
}


def menu ():


    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Cupos por tipo de plan")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. eliminar plan")
    print("6. Salir")
    print("=====================================")
   

def leer_op ():

    while True:
        try:

            op = int(input("ingrese una opcion = "))

            if op > 0 and op <= 6:
                return op
                
            else:
                raise ValueError ("ingrese una opcion valida")
        
        except ValueError:
            print("ingrese una opion valida")

def cuota_t_plan (): 

    inscripcionesconta = 0

    print("ingresa el tipo de plan")
    print("mensual, trimestral o anual")
    try:
        plan = str(input("= "))
        for i in planes:

                if planes [i][1] == plan:
                    
                    inscripcionesconta = inscripcionesconta + inscripciones[i][1]
                    
           
        print(f"la cantidad de {plan} tiene un total de {inscripcionesconta} cuotas ")

    except ValueError:
            print("ingrese l tipo que indica")
            return cuota_t_plan()
    
def busqueda_por_rango(precion_min,preciomax,rango):
    rango == []
    i == 0

    try:

        precion_min == int(input("ingree el precio minimo = "))
        preciomax == int(input("ingrese el precio maximo = "))

        if precion_min > preciomax or precion_min <= 0 or preciomax <= 0:
             raise ValueError ("ingrese los valores correctamnte o valors mayor a 0 ")
        elif precion_min < preciomax:
            for i in inscripciones:
                if inscripciones [i][0]:
                     print(f"{inscripciones}")
                     

                for i in range (precion_min,preciomax):
                     print(f"{i}")

    except ValueError:
         print("error vuelva a intentarlo")

    

while True:

    menu()

    op = leer_op()

    if op == 6:
        print("Programa finalizado")
        break
    elif op == 1:
        cuota_t_plan()
        continue
    elif op == 2:
            busqueda_por_rango()
    elif op == 3:
         print()
         
    elif op == 4:
         print()
         
    elif op == 5:
         print()
         
