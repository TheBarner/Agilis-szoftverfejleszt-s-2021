

// constants won't change. They're used here to set pin numbers:
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

// variables will change:
int buttonState = LOW;         // variable for reading the pushbutton status
int actualstate;

long time =0;
long debounce =200;

String lampregister=String(5);
void setup() {
   Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT); 
 }


void loop() 
{
  // read the state of the pushbutton value:
  actualstate = digitalRead(buttonPin);
  if (Serial.available() > 0)
  {
    // read the incoming byte:
    lampregister = Serial.readStringUntil('\n'); 
     Serial.print("I received: ");      //DEBUG
    Serial.println(lampregister);       //DEBUG
  }
  
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (actualstate==HIGH && millis() - time > debounce)
  {
  
  if(buttonState ==LOW)
  {
   Serial.write("ON\n");
    buttonState = HIGH;
  }
  else
  { 
   
    Serial.write("OFF\n");
     buttonState = LOW;
  }
  time= millis();
  digitalWrite(ledPin, buttonState);

  }
  else
  {
    if(lampregister == "test" )
    {
      digitalWrite(ledPin, HIGH);
      Serial.write ("Lamp request acknowledged\n");
      lampregister ="\n";
      Serial.write("ON\n");
       buttonState = HIGH;
    }
  }
}
