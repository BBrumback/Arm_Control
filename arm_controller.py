import tinyik
import numpy
from ssu_32_interface import Ssu32Interface


class Arm(object):
    def __init__(self, physical_system=False):
        self.ik_solver = self.create_arm()
        self.physical = physical_system
        if self.physical:
            self.ssu32 = Ssu32Interface()

    def create_arm(self):
        base_height = [0., 0., 3.25]
        upper_arm_length = [0., 0., 4.75]
        lower_arm_length = [0., 0., 5.0]
        axis_of_rotation = ['z', 'y', 'y']
        return tinyik.Actuator([axis_of_rotation[0], base_height,
                                axis_of_rotation[1], upper_arm_length,
                                axis_of_rotation[2], lower_arm_length])

    def set_position(self, position, speed):
        angles = self.solve_for_angles_deg(position)
        if self.physical:
            self.ssu32.position_arm(angles, speed)
        else:
            print("Physical system not set, moving to " + angles)

    def solve_for_angles(self, position):
        self.ik_solver.ee = position
        return self.ik_solver.angles

    def solve_for_angles_deg(self, position):
        return numpy.round(numpy.rad2deg(self.solve_for_angles(position)))

    def solve_for_position(self, angles):
        self.ik_solver.angles = numpy.deg2rad(angles)
        return self.ik_solver.ee

    def control_grip(self, width, speed):
        self.sp.write(("#4 P" + str(width) + " S" + str(speed) + "\r").encode())

