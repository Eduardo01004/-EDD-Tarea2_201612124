import os

def Mapeo_col():
    filas=0
    col=0
    print ("Ingrese las dimensiones de la matriz ")
    filas=input("ingrese numero de filas: ")
    col=input("ingrese numero de columnas: ")

    fil=0
    colum=0
    print("posicion a mapear: ")
    fil=input("numero de fila: ")
    colum=input("numero de columna: ")

    resultado=(int(colum)*int(filas))+int(fil)
    GraficaCol(fil,colum,filas,col)
    GColum(fil,colum,filas,col)
    print("el resultado es ")
    print(resultado)

def Mapeo_Fil():
    filas=0
    col=0
    print ("Ingrese las dimensiones de la matriz ")
    filas=input("ingrese numero de filas: ")
    col=input("ingrese numero de columnas: ")

    fil=0
    colum=0
    print("posicion a mapear: ")
    fil=input("numero de fila: ")
    colum=input("numero de columna: ")

    resultado=(int(fil)*int(filas))+int(colum)
    GraficaFil(fil,colum,filas,col)
    Gfila(fil,colum,filas,col)

    print("el resultado es ")
    print(resultado)
def GraficaFil(fila,columna,filas,columnas):
    file = open("mapeo.dot", "w")
    file.write("digraph structs {\nnode [shape=plaintext]\n struct1 "
                    "[label=<\n<TABLE bgcolor=\"gray\">\n")
    for j in range(0,int(filas)):
        file.write("<tr>\n")
        for i in range(0,int(columnas)):
            result=int(j)*int(columnas)+int(i)
            if int(fila)*int(columnas)+int(columna) == int(result):
                file.write(" <td bgcolor=\"red\">("+str(j)+","+str(i)+"):"+str(result)+"</td>\n")
            else:
                file.write(" <td>("+str(j)+","+str(i)+"):"+str(result)+"</td>\n")

        file.write("</tr>\n")

    file.write("</TABLE>\n>];\n}")
    file.close()
    os.system("dot -Tpng mapeo.dot -o mapeo.png")
    os.system("mapeo.png")

def Gfila(fila,columna,filas,columnas):
    file = open("lexi.dot", "w")
    file.write("digraph structs {\n node [shape=plaintext]\n struct1 "
                    "[label=<\n<TABLE bgcolor=\"gray\">\n")
    file.write("<tr>\n")
    for j in range(0,int(filas)):

        for i in range(0,int(columnas)):
            result=int(j)*int(columnas)+int(i)
            if int(fila)*int(columnas)+int(columna) == int(result):
                file.write(" <td bgcolor=\"red\">("+str(j)+","+str(i)+"):"+str(result)+"</td>\n")
            else:
                file.write(" <td>("+str(j)+","+str(i)+"):"+str(result)+"</td>\n")


    file.write("</tr>\n")
    file.write("</TABLE>\n>];\n}")
    file.close()
    os.system("dot -Tpng lexi.dot -o lexi.png")
    os.system("lexi.png")

def GraficaCol(fila,columna,filas,columnas):
    file = open("mapeo2.dot", "w")
    file.write("digraph structs {\nnode [shape=plaintext]\n struct1 "
                    "[label=<\n<TABLE bgcolor=\"gray\">\n")

    for j in range(0,int(filas)):
        file.write("<tr>\n")
        for i in range(0,int(columnas)):
            result=int(i)*int(filas)+int(j)
            if (int(columna)*int(filas))+int(columna) == int(result):
                file.write(" <td bgcolor=\"red\">("+str(j)+","+str(i)+"):"+str(result)+"</td>\n")
            else:
                file.write(" <td>("+str(j)+","+str(i)+"):"+str(result)+"</td>\n")

        file.write("</tr>\n")

    file.write("</TABLE>\n>];\n}")
    file.close()
    os.system("dot -Tpng mapeo2.dot -o mapeo2.png")
    os.system("mapeo2.png")

def GColum(fila,columna,filas,columnas):
    file = open("lexi2.dot", "w")
    file.write("digraph structs {\nrankdir=LR;\n node [shape=plaintext]\n struct1 "
                    "[label=<\n<TABLE bgcolor=\"gray\">\n")
    file.write("<tr>\n")
    for j in range(0,int(columnas)):

        for i in range(0,int(filas)):
            result=(int(j)*int(columnas))+int(i)
            if int(fila)*int(columnas)+int(columna) == int(result):
                file.write(" <td bgcolor=\"red\">("+str(j)+","+str(i)+"):"+str(result)+"</td>\n")
            else:
                file.write(" <td>("+str(j)+","+str(i)+"):"+str(result)+"</td>\n")


    file.write("</tr>\n")
    file.write("</TABLE>\n>];\n}")
    file.close()
    os.system("dot -Tpng lexi2.dot -o lexi2.png")
    os.system("lexi2.png")



while True:
    print("1.mapeo por filas: ")
    print("2.mapeo por columnas: ")
    print("3.Salir ")
    opcion=input("Selecciona una opción: ")
    if opcion=="1":
        Mapeo_Fil()
    elif opcion=="2":
        Mapeo_col()
    elif opcion == "3":
        break
