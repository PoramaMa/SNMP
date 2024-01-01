from pysnmp.hlapi import *

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in bulkCmd(SnmpEngine(),
        CommunityData('public'),
        UdpTransportTarget(('192.168.117.5', 161)),
        ContextData(),0, 25,
        ObjectType(ObjectIdentity('1.3.6.1.2.1'))):
    if errorIndication or errorStatus:
        print(errorIndication or errorStatus)
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
            