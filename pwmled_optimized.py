// Programa para modificar la intensidad de un LED for
int LED=3;                // Salida PWM a utilizar con el LED.
void setup() {
  // Bloque de código de configuración.
  pinMode(LED, OUTPUT);
}
void loop() {
  for(int i=1;i<255;i++){
    analogWrite(LED,i);
    delay(25);
  }
}
