from arm_controller import Arm
from ssu_32_interface import Ssu32Interface

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    control_interface = Ssu32Interface()
    arm = Arm(physical_system=True)

    #angles = arm.set_position([0., 0., 13.], 100)
    arm.set_position([5., 0., 8.], 100)
    #control_interface.set_angle(1, -10, 100)
