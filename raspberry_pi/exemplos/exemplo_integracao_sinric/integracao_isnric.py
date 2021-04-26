import os
import socket
from time import sleep

def sair(erro):
    if(erro ==0):#saida sem erro
        print("Programa finalizado")
        quit()
    elif(erro == 1):#sair com pausa
        print("Programa finalizado")
        os.system("pause")
        quit()

def check_net(url): #testar conexão com internet
    a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.settimeout(.5)
    try:
        b=a.connect_ex((url, 80))
        if b==0: #ok, conectado
            return True
    except:
        pass
    a.close()
    return False

def restart_program():
    os.system(f"python \"{__file__}\"")
    sair(0)

try:
    from sinric import SinricPro
    from sinric import SinricProUdp
except:
    import platform
    if(platform.system()=="Windows"):
        print("SISTEMA OPERACIONAL DETECTADO: WINDOWS")
        print("INSTALANDO BIBLIOTECA PYSINRIC. CONEXÃO À INTERNET NECESSÁRIA")
        os.system("pip install sinricpro")
        restart_program()
    else:
        print("SISTEMA OPERACIONAL DETECTADO: LINUX")
        print("INSTALANDO BIBLIOTECA PYSINRIC. CONEXÃO À INTERNET NECESSÁRIA")
        os.system("pip3 install sinricpro")
        restart_program()
try:
    from credenciais_sinric import appKey, deviceId1, secretKey, deviceIdArr
except:
    print("ARQUIVO COM CREDENCIAIS NÃO ENCONTRADO.")
    sair(1)

def Events():
    while True:
        # Select as per your requirements
        # REMOVE THE COMMENTS TO USE
        # client.event_handler.raiseEvent(deviceId1, 'setPowerState',data={'state': 'On'})
        sleep(2)  # Sleep for 2 seconds


def onPowerState(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state)
    return True, state


eventsCallbacks = {
    "Events": Events
}

callbacks = {
    'powerState': onPowerState
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceIdArr, callbacks,event_callbacks=eventsCallbacks, enable_log=False,restore_states=True,secretKey=secretKey)
    udp_client = SinricProUdp(callbacks,deviceIdArr,enable_trace=False)  # Set it to True to start logging request Offline Request/Response
    client.handle_all(udp_client)
