#include "BlendixSerial.h"

BlendixSerial blendix;
int windspeedPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
 
  int flowSensor = analogRead(windspeedPin);
  float flowBlow = flowSensor/1023.0*1.2;

  if(0.0 <flowBlow){
    float blow = flowBlow * 23.3;  //아래에서 구한 공식을 대입
    if(blow>=0.0&&blow<0.3){//level1
      blendix.setCoordinates(1, 1, 1, 1);
      blendix.setCoordinates(2, 0, 0, 0);
      blendix.setCoordinates(3, 0, 0, 0);
      blendix.setText("level1");
      String Output = blendix.getFormattedOutput();
      Serial.println(Output);
    }
    else if(blow>=0.3 && blow<0.5){//level2
      blendix.setCoordinates(1, 2, 2, 2);
      blendix.setCoordinates(2, 1, 1, 1);
      blendix.setCoordinates(3, 0, 0, 0);
      blendix.setText("level2");
      String Output = blendix.getFormattedOutput();
      Serial.println(Output);
    }
    else if(blow >= 0.5){//level3
      blendix.setCoordinates(1, 3, 3, 3);
      blendix.setCoordinates(2, 2, 2, 2);
      blendix.setCoordinates(3, 1, 1, 1);
      blendix.setText("level3");
      String Output = blendix.getFormattedOutput();
      Serial.println(Output);
    }
  }
  else {  // 전압이 0 미만이면 0.0m/s로 출력 (풍속이 음수가 나오면 안되므로)
    blendix.setCoordinates(1, 0, 0, 0);
    blendix.setCoordinates(2, 0, 0, 0);
    blendix.setCoordinates(3, 0, 0, 0);
    blendix.setText("level0");
    String Output = blendix.getFormattedOutput();
    Serial.println(Output);
  }


  delay(1000);
}