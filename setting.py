class controller_setting:
    def __init__(self):
        self.axis = ["LX", "LY", "RX", "RY"]
        self.button = ["X", "A", "B", "Y", "LB", "RB", "LT", "RT", "BACK", "START", "LS", "RS"]
        self.joystickmin = 15

class serial_setting:
    def __init__(self):
        self.speed = 9600
        self.timeout = 0.1

class camera_setting:
    def __init__(self):
        self.camid = 0
        self.save_dir = './img'