# By: William Pilger
# 2021.08.10 - Song: Heathens (Twenty One Pilots)

import os
import platform
import time
from datetime import datetime

eh_windows = platform.system() == "Windows"
eh_linux = platform.system() == "Linux"

def restart_program():
    if(eh_windows):
        os.system(f"python \"main.py\"")
    elif(eh_linux):
        os.system(f"python3 \"main.py\"")
    quit()
    
def install_lib(lib):
    print(f"\nINSTALANDO BIBLIOTECA NECESSÁRIA, AGUARDE!\n(CONEXÃO COM INTERNET NECESSÁRIA)\n{lib}")
    if(eh_windows):
        os.system(f"pip install {lib}")
    elif(eh_linux):
        os.system(f"pip3 install {lib}")

def limpar_terminal():
    if(eh_windows):
        os.system("cls")
    elif(eh_linux):
        os.system("clear")
    return



def registra_log_geral(texto):
    try:
        with open("log_geral.txt", "a") as arquivo:
            instante = datetime.now().strftime('%d/%m/%Y\t%H:%M:%S')
            arquivo.writelines(f"\n{instante}\t{texto}")
    except:
        pass
    return

def sair(code):
    limpar_terminal()
    if(code == 0):
        print("OOOps! Esta função ainda está em desenvolvimento.\n\nEstamos finalizando.")
        time.sleep(5)
    elif(code == 1):
        print("Você escolheu sair.")
        time.sleep(1)
    elif(code == 2):
        print("Não encontramos o arquivo de configuração necessário.")
        time.sleep(5)
    quit()