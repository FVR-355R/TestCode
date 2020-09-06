#include "vex.h"

using namespace vex;
using signature = vision::signature;
using code = vision::code;

// A global instance of brain used for printing to the V5 Brain screen
brain  Brain;

// VEXcode device constructors
controller Controller1 = controller(primary);
motor LeftFrontMotor = motor(PORT5, ratio18_1, false);
motor LeftBackMotor = motor(PORT6, ratio18_1, false);
motor RightFrontMotor = motor(PORT9, ratio18_1, true);
motor RightBackMotor = motor(PORT20, ratio18_1, true);
motor FeederLeftMotor = motor(PORT3, ratio18_1, false);
motor FeederRightMotor = motor(PORT10, ratio18_1, true);
motor RackAndPinionMotor = motor(PORT8, ratio18_1, false);
motor LiftMotor = motor(PORT1, ratio18_1, true);

// VEXcode generated functions
// define variable for remote controller enable/disable
bool RemoteControlCodeEnabled = true;

/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Text.
 * 
 * This should be called at the start of your int main function.
 */
void vexcodeInit( void ) {
  // nothing to initialize
}