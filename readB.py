from pysnmp.hlapi import *

ip = '192.168.1.111'
oi = '1.3.6.1.4.1.1429.2.2.6.5.11.1.1.4.0'

# acquire satelital decode data C/N margin dB level
def getdB(ip, oi):
    iterator = getCmd(SnmpEngine(),
                    CommunityData('public'),
                    UdpTransportTarget((ip, 161)),
                    ContextData(),
                    ObjectType(ObjectIdentity(oi)))
    varBinds = iterator
    for varBind in varBinds:  
        texto = str(varBind)
        dB = texto[-8:-5]        
    return dB
    
dB = getdB(ip,oi)
print(dB)
