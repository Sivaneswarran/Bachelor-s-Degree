int blue = 13;
int green = 12;
int button = 11;
int buttonState = 0;


void setup() {
  // put your setup code here, to run once:
  pinMode(blue, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(button, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  buttonState = digitalRead(button);

  if (buttonState == 1)
  {
    digitalWrite(blue, HIGH);
    digitalWrite(green, HIGH);
  }

  else if (buttonState == 0)
  {
    digitalWrite(blue, LOW);
    digitalWrite(green, LOW);
  }
}
