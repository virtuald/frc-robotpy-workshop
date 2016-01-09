#!/usr/bin/env python3

import wpilib

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):

        self.joystick = wpilib.Joystick(1)

        self.dio = wpilib.DigitalInput(1)
        self.solenoid1 = wpilib.Solenoid(1)

        self.solenoid4 = wpilib.Solenoid(4)

    def teleopPeriodic(self):
        '''Called every 20ms in teleoperated mode'''
        
        self.solenoid1.set(self.joystick.getTrigger())  # control solenoid via joystick
        self.solenoid4.set(self.dio.get())        # control solenoid via digital I/O

if __name__ == '__main__':
    wpilib.run(MyRobot)


