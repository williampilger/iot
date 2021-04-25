#include <time.h>
#include "ota_firmware.h"
#include "sinric_interface.h"

#define BUILTIN_LED_PIN 2

void setup(){
  Serial.begin(115200);
  Serial.println("Booting");
  pinMode(BUILTIN_LED_PIN, OUTPUT);
  setup_wifi_ota();
  setup_sinric();
}

int ant = millis();
void loop(){
  if(millis()-ant > 2000){
    digitalWrite(BUILTIN_LED_PIN, !digitalRead(BUILTIN_LED_PIN));
    ant = millis();
  }
  handle_wifi_ota();
  handle_sinric();
}
