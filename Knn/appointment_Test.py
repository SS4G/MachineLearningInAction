from KnnUtil import KnnUtil
from config import *
from App_pre import *
class AppointmentTest:
    def __init__(self):
        self.knntool=KnnUtil()
        self.pre=App_pre()
        pass
    def main_test(self):
        self.pre.read_set()
        self.knntool.find_NearestTag_KthNearst()

