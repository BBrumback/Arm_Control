import serial
from logger import Logger


class Ssu32Interface(object):

    def __init__(self):
        self.sp = serial.Serial('/dev/ttyUSB0', 9600)
        self.joint_pulse_home = [0, 1480, 1480]
        self.joint_pulse_range = [0, 810, 900]
        self.joint_offset = [0, 0, 90]
        self.debugger = Logger("SSU32_INTERFACE", debug=True)

    def position_arm(self, angles, speed):
        for number, angle in enumerate(angles):
            self.set_angle(number, angle, speed)
            self.debugger.log("Setting angle of joint_{} to {}".format(number, angle))

    def set_angle(self, pin_number, angle, speed):
        offset_angle = angle - self.joint_offset[pin_number]
        pulse_width = self.angle_to_pulse(offset_angle, pin_number)
        self.set_pwd(pin_number, pulse_width, speed)

    def set_pwd(self, pin_number, pulse_width, speed):
        pin = "#" + str(pin_number)
        pulse = " P" + str(pulse_width)
        speed = " S" + str(speed)
        self.debugger.log(pin + pulse + speed)
        self.sp.write((pin + pulse + speed + "\r").encode())

    def control_grip(self, width, speed):
        self.sp.write(("#4 P" + str(width) + " S" + str(speed) + "\r").encode())

    def angle_to_pulse(self, angle, joint_id):
        angle_ratio_to_max = (angle/90)
        return self.joint_pulse_range[joint_id] * angle_ratio_to_max + self.joint_pulse_home[joint_id]
