#include <Servo.h>

Servo servo1;
Servo servo2;

unsigned long servo1StartTime = 0;
unsigned long servo2StartTime = 0;
bool servo1Active = false;
bool servo2Active = false;

void setup() {
    Serial.begin(9600);
    servo1.attach(9);  
    servo2.attach(10);  

    servo1.write(90);
    servo2.write(90);
}

void loop() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        command.trim();

        if (command == "1") {  
            servo1.write(45);  
            servo1StartTime = millis();
            servo1Active = true;
        } 
        else if (command == "2") {  
            
            servo2.write(45);  
            servo2StartTime = millis();
            servo2Active = true;
        }
    }

    if (servo1Active && millis() - servo1StartTime > 500) {  
        servo1.write(90);
        servo1Active = false;
    }

    if (servo2Active && millis() - servo2StartTime > 500) {  
        servo2.write(90);
        servo2Active = false;
    }
}
