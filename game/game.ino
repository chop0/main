const int ledCount = 10;

int ledPins[] = { 
  2, 3, 4, 5, 6, 7,8,9,10,11 };


void setup() {
  for (int thisLed = 0; thisLed < ledCount; thisLed++) {
    pinMode(ledPins[thisLed], OUTPUT); 
  }
}

void loop() {
  int difficulty = analogRead(A0);
  digitalWrite(2, HIGH);
  delay(difficulty);
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH);
  delay(difficulty);
  digitalWrite(3, LOW);
  digitalWrite(4, HIGH);
  delay(difficulty);
  digitalWrite(4, LOW);
  digitalWrite(5, HIGH);
  delay(difficulty);
  digitalWrite(5, LOW);
  digitalWrite(6, HIGH);
  delay(difficulty);
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  delay(difficulty);
  digitalWrite(7, LOW);
  digitalWrite(8, HIGH);
  delay(difficulty);
  digitalWrite(8, LOW);
  int pin = 8;
  pin+-1;
  if (digitalRead(10) == HIGH) {
    digitalWrite(8, HIGH);
    if (pin == 8) {
      int theLed = 2;
      Serial.write("You won!");
      while (true) {
        if (theLed == 8) {
          theLed+-6;
        }
      digitalWrite(ledPins[theLed], HIGH);
      delay(500);
      digitalWrite(ledPins[theLed], LOW);
      delay(500);
      theLed++;
      }
    }
  }
  delay(difficulty);
  pin++;
}

