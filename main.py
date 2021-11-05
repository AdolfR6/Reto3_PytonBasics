
Billetes=[500,200,100,50,20,10,5]
Monedas=[2,1,0.5,0.2,0.10,0.05,0.02,0.01]
Carta=[]
Precio=[]
midiccionario={}
Pedido=[]
Coste_pedido=0
Seguir_pidiendo=1
Num_Carta=[1,2,3,4,5,6,7,8,9,10]

print("Introduce 10 platos para crear una carta:")

for i in Num_Carta:

    Nombre_plato=input("Introduce el nombre de un plato ")
    Carta.append(Nombre_plato)

    Precio_plato=float(input("Introduce el precio del plato "))
    Precio.append(Precio_plato)
    midiccionario[Nombre_plato]=Precio_plato

#print(midiccionario)

print("Esta es la carta:")

for x,y in zip(Carta,Precio):
    print(x,"-",y, " €")

while Seguir_pidiendo==1:
    Comanda=input("¿Que quieres cenar? ")
    Pedido.append(Comanda)
    Continuar=input("¿Quieres seguir pidiendo? ")

    if Continuar=="Si" or Continuar=="si" or Continuar=="S" or Continuar=="s" :
        Seguir_pidiendo=1

    elif Continuar=="No" or Continuar=="no" or Continuar=="N" or Continuar=="n" :
        Seguir_pidiendo = 0
        break
    else:
        print("No le he entendido.")
        Seguir_pidiendo = 1


#print(Pedido[0])

for n in Pedido:
#   print(n)
    if n in Carta:
        Coste_pedido=Coste_pedido + midiccionario[n]
    else:
        print(n,"no está en la carta")

print("Tienes que pagar", Coste_pedido)

for i in Billetes:
    if Coste_pedido >= i:
        Restante = Coste_pedido // i
        print("Abona con " + str(int(Restante)) + " billestes de " + str(i) + " €")
        Coste_pedido = Coste_pedido % i

for i in Monedas:
    if Coste_pedido >= i:
        Restante = Coste_pedido // i
        print("Abona con " + str(int(Restante)) + " monedas de " + str(i) + " €")
        Coste_pedido = Coste_pedido % i