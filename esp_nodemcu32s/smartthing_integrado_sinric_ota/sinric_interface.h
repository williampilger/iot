#include <SinricPro.h>
#include <SinricProSwitch.h>
#include "sinric_credenciais.h"

void setupSinricPro();
bool LampadaState(const String &deviceId, bool &state);


// main setup function
void setup_sinric(){
  void setupSinricPro();
  bool DeviseState(const String &deviceId, bool &state);
  setupSinricPro();
  pinMode(Device_Pin, OUTPUT);
}

void handle_sinric() {
  SinricPro.handle();
}

bool DeviceState(const String &deviceId, bool &state) {
  Serial.printf("O dispositivo foi %s\r\n", state?"ligado":"desligado");
  digitalWrite(Device_Pin, state);
  return true;
}

void setupSinricPro() {
  SinricProSwitch &mySwitch2 = SinricPro[Device_ID];
  mySwitch2.onPowerState(DeviceState);

  // setup SinricPro
  SinricPro.onConnected([](){ Serial.printf("Conectado a nuvem SinricPro\r\n"); }); 
  SinricPro.onDisconnected([](){ Serial.printf("Desconectado a nuvem SinricPro\r\n"); });
  SinricPro.begin(APP_KEY, APP_SECRET);
}
