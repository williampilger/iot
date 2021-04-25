#include <WiFi.h>   
#include <SinricPro.h>
#include <SinricProSwitch.h>
#include "credenciais.h"

#define Lampada_ID       "60858813d3827f1ea82d1a89"
#define Lampada_Pin 15

#define BUILTIN_LED_PIN 2

#define BAUD_RATE         9600                // Se precisar, pode trocar o baud rate


void setupWiFi();
void setupSinricPro();
bool LampadaState(const String &deviceId, bool &state);


// main setup function
void setup() {
  Serial.begin(BAUD_RATE); Serial.printf("\r\n\r\n");
  setupWiFi();
  setupSinricPro();
  pinMode(Lampada_Pin, OUTPUT);
  pinMode(BUILTIN_LED_PIN, OUTPUT);
  digitalWrite(BUILTIN_LED_PIN, LOW);
}

void loop() {
  SinricPro.handle();
  digitalWrite(BUILTIN_LED_PIN, HIGH);
}

bool LampadaState(const String &deviceId, bool &state) {
  Serial.printf("A lampada foi %s\r\n", state?"ligada":"desligada");
  digitalWrite(Lampada_Pin, state);
  return true; // request handled properly
}

// setup das conexões Wifi
void setupWiFi() {
  Serial.printf("\r\n[Wifi]: Conectando...");
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.printf(".");
    delay(250);
  }

  Serial.printf("Conectado!\r\n[WiFi]: Endereço de IP e %s\r\n", WiFi.localIP().toString().c_str());
}

// setup das funções para o SinricPro
void setupSinricPro() {
  SinricProSwitch &mySwitch2 = SinricPro[Lampada_ID];
  mySwitch2.onPowerState(LampadaState);

  // setup SinricPro
  SinricPro.onConnected([](){ Serial.printf("Conectado a nuvem SinricPro\r\n"); }); 
  SinricPro.onDisconnected([](){ Serial.printf("Desconectado a nuvem SinricPro\r\n"); });
  SinricPro.begin(APP_KEY, APP_SECRET);
}
