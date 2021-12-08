// constants won't change. They're used here to set pin numbers:
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

// variables will change:
int buttonState = LOW;         // variable for reading the pushbutton status
int actualstate;

long time =0;
long debounce =200;
String lampregister=String(500);
void setup() {
   Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT); 
 }
 
void ledInv()
{
   buttonState = ~buttonState;
   digitalWrite(ledPin, buttonState);
}

void readSerial()
{
  lampregister = Serial.readStringUntil('\n'); 
}

void checkSerial()
{
    if(lampregister == "test" )
    {
      Serial.write ("Lamp request acknowledged\n");
      lampregister ="\n";
      buttonStateFunct();
    }
}
void buttonStateFunct()
{
    if(!buttonState)
      Serial.write("ON\n");
    else
      Serial.write("OFF\n");
  ledInv();
}
void debug()
{
    Serial.print("I received: ");      //DEBUG
    Serial.println(lampregister);       //DEBUG
}
void serial()
{
   if (Serial.available() > 0)
  {
    // read the incoming byte:
    readSerial();
    debug();
  }
}
bool buttonActuallyPressed()
{
   // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (actualstate==HIGH && millis() - time > debounce)
  {
    buttonStateFunct();
  time= millis();
  return true;
  }
  else
  return false;
}
void loop() 
{
  // read the state of the pushbutton value:
  actualstate = digitalRead(buttonPin);
  serial();
  if(!buttonActuallyPressed())
  checkSerial();
}
