# Instalando e configurando o OS na Raspberry Pi

## Usando Raspi Imager

Caso queira utilizar a ferramenta automática para criação do SD Card, acesse [o site oficial](https://www.raspberrypi.org/software/) e procure pelo instalador do Raspi Imager.

Se estiver usando linux, poderá instalá-la usando:

> sudo apt install rpi-imager

## Baixando imagem e criando mídia manualmente (standallone)

- Baixe a imagem de sistema desejada na [página de downloads](https://www.raspberrypi.org/software/operating-systems/)
- Baixe também o Balena Etcher, disponível no [site oficial](https://www.balena.io/etcher/?)
- Extraia a imagem que acabou de baixar;
- Execute o Balena Etcher;
- Selecione **Flash from file** e navegue até a ISO que você extraiu;
- Insira e selecione o cartão SD que deseja utilizar (aconselhamos o uso de SD classe 10);
- Clique em **Flash** e digite sua senha de administrador, caso necessário.

## Ativando o servidor SSH

Você pode ativá-lo sem ter acesso à area de trabalho da Raspberry criando um arquivo vazio na partição **boot** com o nome de **ssh**.

## Instalando interface gráfica na versão lite

Bom, pode ser necessário instalara a interface gráfica após você já ter configurado a versão lite do OS. Para isso use:

> sudo apt install xserver-xorg

> sudo apt install raspberry-ui-mods

> reboot

