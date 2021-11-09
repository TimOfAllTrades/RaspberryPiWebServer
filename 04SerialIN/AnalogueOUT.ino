//Let's see what we can do with these RGB LEDs
//Note that these LEDs are connected individually so you can't use them as if the 2 leds are an led "strip"

//include AdaFruit's RGB Library

//These are the arduino pins that contain those 2 RGB leds..
//We are only going to use the second one in this example
#define RGB1 12
#define RGB2 13

//Define sensor pins
#define SENSOR_1_PIN A0
#define SENSOR_2_PIN A1
#define SENSOR_1_OUTPUT 3
#define SENSOR_2_OUTPUT 4

//Now we have to set them up!
// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:


void setup(){
  //Let's use the serial monitor.
  Serial.begin(9600);

  // Initiate digital pins as outputs.
  pinMode(SENSOR_1_OUTPUT, OUTPUT);
  pinMode(SENSOR_2_OUTPUT, OUTPUT);
  
}

void loop(){

int SENSOR_1_VALUE = analogRead(SENSOR_1_PIN);
  int SENSOR_2_VALUE = analogRead(SENSOR_2_PIN);
  Serial.println(SENSOR_1_VALUE);
  delay(500);
}
