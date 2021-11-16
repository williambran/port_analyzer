#!/usr/bin/python3
import requests
import validators
import re

def vlidateVersionIP(ip):
    typeIp = validators.ip_address.ipv4(ip)
    if typeIp:
        return {'typeIP':'IP Versionn 4','isIP':True}
    elif validators.ip_address.ipv6(ip):
        return {'typeIP':'IP Versionn 6','isIP':True}
    else:
        return {'typeIP':'No es IP','isIP':False}




def probarURL(path, isIp):
    
    protocolo = "http://"
    urlpas = path
    isurl = isIp
    if not(isIp):
       try:
           request = requests.get(protocolo + urlpas, stream = True, timeout=5)
           print("wito SUCCEFUL")
           return True

       except requests.exceptions.HTTPError as err:
           print("wito EXCEPTION",err)
       except requests.exceptions.RequestException as err:
           print("OOps: Something Else",isIp ,err)
           return False
    else:
        return False 
  ## typeIp = validators.ip_address.ipv4(path)
  #  typeIp6 = validators.ip_address.ipv4(path)





def validateForm(target):
    path = target
    

    #Validar si trae la http:
    patron = re.compile('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')
    patronIPV4 = re.compile('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    if patron.match(path):
        patchSinProtocolo = path.split("://")
        path = patchSinProtocolo[1]
        typeIP = vlidateVersionIP(path) 
        isIP = typeIP.get('isIP')
        pruebaURL = probarURL(path,isIP)
        typeIP.setdefault('isURL',pruebaURL)
        typeIP.setdefault('path',path)
        print("pruebas",typeIP)
        return typeIP

    else:
        print("Es una IP", path)
        typeIP = vlidateVersionIP(path)
        isIP = typeIP.get('isIP')
        pruebaURL = probarURL(path, isIP)
        typeIP.setdefault('isURL', pruebaURL)
        typeIP.setdefault('path',path)
        print("pruebas",typeIP)
        return typeIP

   


        #tipoIP = validators.ip_address.ipv6("127.0.0.1")
        #print("Tipo de ip",tipoIP)

