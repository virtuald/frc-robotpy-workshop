try:
    import wpilib
except ImportError:
    from pyfrc import wpilib

class MyRobot(wpilib.IterativeRobot):
    
    def __init__(self):
        super().__init__()

        self.joystick = wpilib.Joystick(1)

        self.dio = wpilib.DigitalInput(1)
        self.dio.label = "Device label in simulator"

        self.solenoid1 = wpilib.Solenoid(1)
        self.solenoid1.label = "CUSTOM LABEL IN SIMULATOR"

        self.solenoid4 = wpilib.Solenoid(4)
        self.solenoid4.label = "ANOTHER LABEL"

    def TeleopPeriodic(self):
        '''Called every 20ms in teleoperated mode'''

        self.solenoid1.Set(self.joystick.GetTrigger())  # control solenoid via joystick
        self.solenoid4.Set(self.dio.Get())              # control solenoid via digital I/O


def run():
    robot = MyRobot()
    robot.StartCompetition()
    return robot


if __name__ == '__main__':
    wpilib.run()


