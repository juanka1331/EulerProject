def imprime(vector):
   "function_docstring"
   print("Vector: {0}, Longitud: {1}.".format(vector, len(vector)))
   return


def is_div_list(list_num, div):
    "Given a list of number, this functions gives back the function" \
    "of numbers which are divisibles between div"
    return [i for i in list_num if i % div == 0]


def is_div(num, div):
    return 0 == num % div

def next_prime_factor():
    pass

def factores_primos(siguiente):

    fin = 0;
    inicio = 2;
    resultado = []

    while(fin == 0):

        valor_dividir = siguiente
        #print("Valor: {}".format(valor_dividir))
        limite = int((siguiente/2) + 1)


        for x in range(inicio, limite, 1):
            #print("Bucle principal: {}".format(x))

            if((valor_dividir % x) == 0):
            #    print("Divisible por: {}".format(x))
                siguiente = int(valor_dividir / x)

                #print("Nuevo: {}".format(siguiente))
                resultado.append(x)

                break


        if(x == (limite - 1)):
            fin = 1
            resultado.append(valor_dividir)
            inicio = resultado  #para acelerar el proceso

    return resultado


#Dado un vector de factores primos, obtiene los posibles multiplos
#hasta un maximo
#
# def multiplos(v_factores, maximo):
#
#     nada = maximo
#     index = 0
#     resultado = []
#     print("longitud multiplos: {}".format(len(v_factores)))
#
#     for mul in range(1, len(v_factores) + 1, 1):  # Indica el numero de multiplicaciones
#
#          for i in range(0, len(v_factores), 1):
#              resultado.append(1)
#              index = len(resultado) - 1
#              print("nuevo, mul: {}, i: {}".format(mul,i))
#
#              for x in range(0, mul, 1):  # multip
#                  resultado[index] = resultado[index] * v_factores[x]
#                  print("next: {}".format(resultado))
#
#
#
#     return [resultado]

# def get_count(v):
#
#     resultado = []
#
#     for i in range (0, len(v), 1):
#         encontrado = 0
#         for i in range(0, len(resultado,1))
#             encontrado = 1
#             resultado.append([1,1]):
#             break
#
#         if(encontrado == 1):
#
#         else
#
#     return resultado


#def is_(list_num, div_list):
#    for i in div_list:
#        list_num = is_div(list_num, i)
#
#    return list_num