#define BLYNK_TEMPLATE_ID "BLYNK_TEMPLATE_ID"
#define BLYNK_TEMPLATE_NAME "BLYNK_TEMPLATE_NAME"
#define BLYNK_AUTH_TOKEN "BLYNK_AUTH_TOKEN"

/* Comment this out to disable prints and save space */
#define BLYNK_PRINT Serial

#include <BlynkSimpleEsp32.h>

// Your WiFi credentials.
// Set password to "" for open networks.
//DONT CHANGE IF YOU USE THIS CODING ON WOKWI 

char ssid[] = "Wokwi-GUEST";    //CHANGE TO YOUR OWN WIFI NAME
char pass[] = "";               // CHANGE TO YOUR OWN WIFI PASSWORD

int blue = 12;
int green = 14;

BLYNK_WRITE(V0) //for blue led
{
  int buttonState = param.asInt();

  if(buttonState == 1)
  {
    digitalWrite(blue, HIGH);
  }

  if(buttonState == 0)
  {
    digitalWrite(blue, LOW);
  }
}

BLYNK_WRITE(V1) //for green led
{
  int buttonState = param.asInt();

  if(buttonState == 1)
  {
    digitalWrite(green, HIGH);
  }

  if(buttonState == 0)
  {
    digitalWrite(green, LOW);
  }
}


void setup() 
{
  Serial.begin(115200);

  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);

  pinMode(blue, OUTPUT);
  pinMode(green, OUTPUT);

  digitalWrite(blue, LOW);
  digitalWrite(green, LOW);

}

void loop() 
{
  Blynk.run();

}
