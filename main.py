import scanner #librería a utilizar para scannear puertos
import helperValidator





def menu():
    offSet = 0
    while offSet == 0:
        entrada = input("Selecciones que funcion quiere realizar \n [1] Funcion basica \n [2] Determinados puertos  \n [3] Verbosidad \n ")
        #Validar que la entrada sea una url o una ip, sin puerto
        if entrada == "1" or entrada == "2" or entrada == "3":
            parametrosArr =  seleccionarParametros(entrada)
            
            if entrada == "3":
                parametrosArr[3] = 1
            
            ports = scanner.getOpenPorts(parametrosArr[0],[parametrosArr[1],parametrosArr[2]], parametrosArr[3])
            if ports:
                offSet = 1
                print("Open ports basic:", ports)
            else:
                print("\n No se encontraron puertos abiertos o fue incorrecta la ip \nintenta con otra ip/host o un mayor rango de puertos")
                offSet = 0

        else:
            print("Ingresa un valor valido")
            offSet = 0


def seleccionarParametros(tipoEntrada):
    arr = []
    numeroEntradas = int(tipoEntrada)
    parameters = parametros(numeroEntradas)
    for i in parameters:
        if i != 0:
            indixParametro = parameters.index(i)
            wito = 0
            while wito == 0:
                entradasParametros = input(i)
                
                if indixParametro == 1 or indixParametro == 2:
                    try:
                        entradasINT = int(entradasParametros)
                        if indixParametro == 1:
                            arr.append(entradasINT)
                            wito = 1
                            
                        elif indixParametro == 2 and (entradasINT <= arr[1] or entradasINT > 65535):
                            print("Ingresa un valor valido mas alto que el rano de inicio y menos a 65535")
                            wito = 0
                        else:
                            print("Debo pasar 1 vez wito")
                            arr.append(entradasINT)
                            wito = 1
                    except:
                        print("Ingresa un valor valido para este parametro",arr)
                        wito = 0
                else:
                    
                    wito = 1
                    arr.append(entradasParametros)
                         
                
            
            

        else:
            arr.append(0)
    print("ANTES DE ENVIAR", arr)
    return arr



def parametros(parametros):
    
    params = {1:["Ingresa la url o ip"],2 :[ "Selecciona el inicio de los puertos", "Selecciona el final de los puertos"], 3: ["Se generaran los nombres de los puertos, enter para continuar"]}
    sendParameter = []
    for i in range(1, 4 ):
        parametrosArr = params.get(i)
        for param in parametrosArr:
            if i <= parametros:
                sendParameter.append(param)
            else:
                sendParameter.append(0)
    return sendParameter

menu()


# Ejemplo de función básica
#ports = scanner.getOpenPorts("yopublico.mx",[])
#print("Open ports basic:", ports)

# Determinando Puertos
#ports = scanner.getOpenPorts("unam.mx", [79, 82])
#print("Open ports range given:", ports)

# Verbosidad

#entrada = input("ingresa ip,URL o lo que sea : ")
#ports = scanner.getOpenPorts(entrada, [7,8443], True)
#print("Open ports range give + verbose:", ports)
