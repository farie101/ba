import unittest
from PIL import Image
from run_FH_algorithm import FH_run

from Absolute_Intensity import AbsoluteIntensity
class test_FHRun(unittest.TestCase):
    def setUp(self):
        self.img = Image.open("Images/bsd_l_chicken.jpg")
        self.img1 = Image.open("Images/bsd_l_surfer.jpg")
    def test1(self):
        fh = FH_run(self.img, 1000000, self.img.mode, False, AbsoluteIntensity)
        merge = fh.step_3()

        print(f"Final number of components: {len(merge)}")
    def test2(self):
        fh = FH_run(self.img, 100000, self.img1.mode, False, AbsoluteIntensity)
        merge = fh.step_3()


