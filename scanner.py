#!/usr/bin/python3

import socket #library to use https://docs.python.org/3/library/socket.html
import helperValidator
from ports import ports_and_services

def getOpenPorts(target, portRange = [],verbose = False):
    openPorts = []
    strValidate = ""

    #Valida si es ipv4 o ipv6
    #Validar target para url
    response = helperValidator.validateForm(target)
    print("veamos el path", response.get('path'))
    analisisHost = response.get('path')
    
    
    #Obtener el host con socket YA
    try:
        host = socket.gethostbyname(analisisHost)
        print("ESTE ES EL HOST",host )
    except:
        print("no se pudo optener")
        return openPorts


    
    
    #hacer un loop sobre el rango de puertos
    # true si trae rango final
    if portRange[1] != 0:
        for i in range(portRange[0],portRange[1]+1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            #abrir el socket determinado
            conec = sock.connect_ex((host,i))
            
            # 0 si se logro conectar
            if not(conec):
                puertoString = str(i)
                print("Se conecto al puerto" + puertoString)
                #true si queremos verbossidad
                if verbose:
                   puertosAbiertosVervosidad = ports_and_services.get(i)
                   if puertosAbiertosVervosidad == None:
                       puertosAbiertosVervosidad = "Sin informacion del puerto"
                   puertosAbiertosVervosidad = puertosAbiertosVervosidad + " Puerto: " +  puertoString
                   openPorts.append(puertosAbiertosVervosidad)
                  # print("informacioncion de puerto", informacion)
                else:
                    openPorts.append(i)
            #Si no se conecta  aningun puerto falta enviarle algo
    # Si el rango de inicio y final es igual a 0 --- Se hara un loop de portos basicos
    elif portRange[0] == 0 and portRange[1] == 0:
        for i in ports_and_services:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conectionSuccess = sock.connect_ex((host,i))
            if conectionSuccess == 0:
                puertosAbiertos = ports_and_services.get(i)
                openPorts.append(puertosAbiertos)



    #verificar si se conecta

    return openPorts

