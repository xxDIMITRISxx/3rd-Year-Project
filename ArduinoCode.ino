#include "BraccioV2.h"
Braccio arm;
//Set these values from the min/max gripper joint values below.
#define GRIPPER_CLOSED 85
#define GRIPPER_OPENED 25
int number;
int angleNumber;
boolean ifGripperOpen;

void setup() {
  Serial.begin(9600);
  Serial.println("Initializing... Please Wait");//Start of initialization, see note below regarding begin method.

  //Update these lines with the calibration code outputted by the calibration program.
  arm.setJointCenter(WRIST_ROT, 90);
  arm.setJointCenter(WRIST, 90);
  arm.setJointCenter(ELBOW, 90);
  arm.setJointCenter(SHOULDER, 90);
  arm.setJointCenter(BASE_ROT, 90);
  arm.setJointCenter(GRIPPER, 25);//Rough center of gripper, default opening position

  ifGripperOpen = true; //set this value to true when it the program start again
  
  //Set max/min values for joints as needed. Default is min: 0, max: 180
  //The only two joints that should need this set are gripper and shoulder.
  arm.setJointMax(GRIPPER, 100);//Gripper closed, can go further, but risks damage to servos
  arm.setJointMin(GRIPPER, 15);//Gripper open, can't open further

  arm.begin(true);// Start to default vertical position.
  //This method moves the arm to the values specified by setJointCenter
  //and by default will make the arm be roughly straight up.

  //NOTE: The begin method takes approximately 8 seconds to start, due to the time required
  //to initialize the power circuitry.
  Serial.println("Initialization Complete");
}

void loop() {
  arm.safeDelay(1000);
  int joint;
  Serial.println("===============================");
  Serial.println("Wrist-rotation - 1");
  Serial.println("Wrist-vertical-rotation - 2");
  Serial.println("Elbow - 3");
  Serial.println("Base - 4");
  Serial.println("Open/Close Gripper - 5");
  Serial.println("Give number of joint!!!");
  Serial.println("===============================");
  Serial.println(joint);
  while (!Serial.available());
  number = Serial.readString().toInt();
  //Check if the input is the specific gestures
  while (number < 0 || number > 5) {
    while (!Serial.available());
    number = Serial.readString().toInt();
  }
  joint = returnJoint(number);
  if (number == 5) {
    if (ifGripperOpen == true) {
      arm.safeDelay(1000);
      closeGripper();
    } else {
      arm.safeDelay(1000);
      openGripper();
    }
    ifGripperOpen = !ifGripperOpen;
  } else {
    Serial.println("Give number to choose the angle number to move the joint :");
    while(!Serial.available());
    angleNumber = Serial.readString().toInt();
    movement(joint, angleNumber);
    arm.safeDelay(1000);
  }
}

void openGripper(){
  //Set the gripper position to open
  arm.setOneAbsolute(GRIPPER, GRIPPER_OPENED);
}

void closeGripper(){
  //Set the gripper position to closed
  arm.setOneAbsolute(GRIPPER, GRIPPER_CLOSED);
}

void movement(int joint, int angleNum) {
  arm.safeDelay(1000);
  arm.setOneAbsolute(joint,angleNum);
}

int returnJoint(int x) {
  if (x == 1) {
    return WRIST_ROT ;
  }else if (x == 2) {
    return WRIST;
  }else if (x == 3) {
    return ELBOW;
  }else if (x == 4) {
    return BASE_ROT;
  }else if (x == 5) {
    return GRIPPER;
  } else {
    return 0;
  }
}
