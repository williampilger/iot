import os
import socket
from time import sleep

def sair(erro):
    if(erro ==0):#saida sem erro
        print("Programa finalizado")
        quit()
    elif(erro == 1):#sair com pausa
        print("Programa finalizado\n\nPressione ENTER para encerrar.")
        input()
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
    import platform
    if(platform.system()=="Windows"):
        os.system(f"python \"{__file__}\"")
    else:
        os.system(f"python3 \"{__file__}\"")
    sair(0)

try:
    from sinric import SinricPro, SinricProUdp
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

with open("credenciais_sinric.txt", "rt") as arquivo:
    x = 0
    deviceIdArr = []
    for linha in arquivo:
        if(x == 0):
            appKey = linha[:len(linha)-1]#remove \n
        elif(x == 1):
            secretKey = linha[:len(linha)-1]#remove \n
        else:
            tamlin = len(linha)
            if(linha[tamlin-1] == "\n"):
                tamlin -= 1#remove \n se tiver
            deviceIdArr.append(linha[:tamlin])
        x += 1
    if(x < 2):
        print("FALHA AO CARREGAR CREDENCIAIS SINRIC")
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
    sair(0)
