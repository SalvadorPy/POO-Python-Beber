from gaseosas import gaseosas
from hidratantes import hidratantes
from energizantes import energizantes


def recoleccion():
    mililitros = int(input("Ingresa los mililitros: \n"))
    sabor = str(input("Ingresa el sabor: \n"))
    compannia = str(input("Ingresa la compañía:\n"))
    fecha_caducidad = str(input("Ingresa la fecha de caducidad(DD/MM/AAAA):\n"))
    tipo_bebida = int(input("Ingresa el tipo de bebida:\n1.-Hidratante\n2.-Energizante\n3.-Gaseosa\n"))

    if(tipo_bebida == 1):
        cantidad_electrolitos = int(input("Ingresa la cantidad de electrolitos:\n"))
        hidratanteEnCurso = hidratantes(mililitros, sabor, compannia, fecha_caducidad, cantidad_electrolitos)
        
        bebidasHidratantes.append(hidratanteEnCurso)

    elif(tipo_bebida == 2):
        cantidad_cafeina = int(input("Ingresa la cantidad de cafeina(mg):\n"))
        energizanteEnCurso = energizantes(mililitros, sabor, compannia, fecha_caducidad, cantidad_cafeina)
        
        bebidasEnergizantes.append(energizanteEnCurso)

    elif(tipo_bebida == 3):
        cantidad_sellos = int(input("Ingresa la cantidad de sellos de salud:\n"))
        gaseosaEnCurso = gaseosas(mililitros, sabor, compannia, fecha_caducidad, cantidad_sellos)
        
        bebidasHidratantes.append(gaseosaEnCurso)




bebidasGaseosas = []
bebidasHidratantes = []
bebidasEnergizantes = []
agregar=str(input("Quieres agregar Bebida:"))
while agregar=="Si":
    recoleccion()
    agregar=str(input("Quieres agregar Bebida:"))

y=1
if bebidasGaseosas:

    for x in bebidasGaseosas:
        print("\t\t\tBebida Gaseosa"+ str(y))
        print(x)
        y+=1
if bebidasEnergizantes:

    print("\t\t\tBebida Energizante"+ str(y))
    for x in bebidasEnergizantes:
        print(x)
        y+=1
if bebidasHidratantes:
    
    print("\t\t\tBebida Hidratante"+ str(y))
    for x in bebidasHidratantes:
        print(x)
        y+=1



