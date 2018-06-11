

#pragma systemFile

/*
IMPLEMENT ALL!!!
Calibrate to scale
Use Linear Interpolation
*/

int readTemp(){
	int x = SensorValue(tempSensor)
  return x;
}
/*
Return SensorValue
*/
int readLight(){
	int x = SensorValue(lightSensor)
	return x;
}
/*
Return SensorValue for light
*/
int readSalt(){
	int x = SensorValue(saltSensor)
  return x;
}

/*
FIND Cutoff values
0: OFF
1: LOW
2: MED
3: HIGH
*/
int readWind(){
	int x = abs(SensorValue(windSensor)) //Read absolute value of rotations
  return x;
}
