import os
import asyncio
from dotenv import load_dotenv
from pysnmp.hlapi import *

load_dotenv()
USERNAME = os.getenv('USERNAME_DEV')
PASSWORD = os.getenv('PASSWORD_DEV')
# print(USERNAME, PASSWORD)

list_ip = ['192.168.20.1', '192.168.20.2', '192.168.20.3', '192.168.20.4']
# ip_address = '192.168.20.1'
# iterator = getCmd(SnmpEngine(),
#                     CommunityData('public'),
#                     UdpTransportTarget(('demo.snmplabs.com', 161)),
#                     ContextData(),
#                     ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

for ip in list_ip:
    logiC = getCmd(
        SnmpEngine(), 
        CommunityData('mytest'),
        UdpTransportTarget((ip, 161)),
        ContextData(), 
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
    )
    print(logiC)

    # if errorIndication:
    #     print(errorIndication, file=sys.stderr)
    #     break
    # elif errorStatus:
    #     print('%s at %s' % (errorStatus.prettyPrint(),
    #                         errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), 
    #                         file=sys.stderr)             
    #     break
    # else:
    #     for varBind in varBinds:
    #         print(varBind)


    # errorIndication, errorStatus, errorIndex, varBinds = next(
    #     getCmd(SnmpEngine(),
    #            CommunityData('mytest', mpModel=0),
    #            UdpTransportTarget((ip, 161)),
    #            ContextData(),
    #            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
    # )
    # print("\nFetching stats for...", server_ip)
    # for varBind in varBinds:
    #     print (varBind[1])



# async def run():
#     ip = '192.168.20.1'

#     snmpEngine = SnmpEngine()
#     errorIndication, errorStatus, errorIndex, varBinds = await sendNotification(
#         snmpEngine,
#         CommunityData('mytest', mpModel=0),
#         await UdpTransportTarget.create((ip, 161)),
#         ContextData(),
#         ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
#     )

#     if errorIndication:
#         print(errorIndication)

#     snmpEngine.closeDispatcher()

# asyncio.run(run())