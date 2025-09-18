# import library for robot programming
import wpilib
import wpilib.drive
import rev

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Define what gamepad I'm using
        self.pad = wpilib.XboxController(0)

        # Define drive motors 
        self.motor_left_1 = rev.SparkMax(2, rev.SparkMax.MotorType.kBrushless)
        self.motor_left_2 = rev.SparkMax(3, rev.SparkMax.MotorType.kBrushless)
        self.motor_right_1 = rev.SparkMax(4, rev.SparkMax.MotorType.kBrushless)
        self.motor_right_2 = rev.SparkMax(5, rev.SparkMax.MotorType.kBrushless)

        # Set the right side to be inverted
        self.motor_right_1.setInverted(True)  # Set right 1 inverted
        self.motor_right_2.setInverted(True)  # SEt right 2 inverted

        # Combine motors into groups
        self.left_group = wpilib.MotorControllerGroup(self.motor_left_1, self.motor_left_2)
        self.right_group = wpilib.MotorControllerGroup(self.motor_right_1, self.motor_right_2)

        # Define drivetrain
        self.drivetrain = wpilib.drive.DifferentialDrive(self.left_group, self.right_group)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        # This function gets called over and over again during teleoperated mode

        # 1. Read button / joystick
        left_y = self.pad.getLeftY()
        right_y = self.pad.getRightY()

        if left_y > 0.4:
            left_y = 0.4
        elif left_y < -0.4:
            left_y = -0.4

        if right_y > 0.4:
            right_y = 0.4
        elif right_y < -0.4:
            right_y = -0.4

        # 3. Turn motors
        self.drivetrain.tankDrive(left_y, right_y)


if __name__ == "__main__":
    wpilib.run(MyRobot)

# Dylan was here