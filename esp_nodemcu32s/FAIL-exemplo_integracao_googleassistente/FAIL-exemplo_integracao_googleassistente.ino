#include "ota_firmware.h"

void setup(){
  Serial.begin(115200);
  Serial.println("Booting");
  wifi_ota_inicializa();
  
}

void loop(){
  ota_handle();
  
}
