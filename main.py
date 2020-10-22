print ("Todas las notas son sobre 100")         #GUÍA USUARIO

N1 = float (input ("Introduzca nota 1: "))      #PIDE VALOR
N2 = float (input ("Introduzca nota 2: "))      #PIDE VALOR
N3 = float (input ("Introduzca nota 3: "))      #PIDE VALOR
N4 = float (input ("Introduzca nota 4: "))      #PIDE VALOR

Media = (N1+N2+N3+N4)/4     #MEDIA

if Media >=90:      #MEDIA MAYOR A 90
    print ("La nota es equivalente a una A")                     #OUPTPUT
else:       #SI NO
    if Media >= 80:     #MEDIA MAYOR A 80
        print ("La nota es equivalente a una B")                #OUTPUT
    else:       #SI NO
        if Media >= 70:     #MEDIA MAYOR A 70
            print ("La nota es equivalente a una C")           #OUTPUT
        else:       #SI NO
            if Media >=60:      #MEDIA MAYOR A 60
                print ("La nota es equivalente a una D")       #OUTPUT
            else:       #EL RESTO (MENORES DE 60)
                print("La nota es equivalente a una E")         #OUTPUT