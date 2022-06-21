import multiplat as mp
import sinric_devices as sd
import asyncio

try:
    from sinric import SinricPro
except:
    mp.install_lib('sinricpro')
    mp.restart_program()

try:
    from credenciais_sinric import appKey, secretKey, deviceArr
except:
    print("ARQUIVO COM CREDENCIAIS NÃO ENCONTRADO OU INVÁLIDO.")
    mp.sair(1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for device in deviceArr:
        if(device['Type'] == 'switch'):
            client = SinricPro(appKey, [device['ID']], sd.switch_callbacks, enable_log=True, restore_states=False, secretKey=secretKey)
            loop.run_forever(client.connect())
        else:
            print("TIPO DE DISPOSITIVO INVÁLIDO.")

# To update the power state on server. 
# client.event_handler.raiseEvent(tvId, 'setPowerState',data={'state': 'On'})