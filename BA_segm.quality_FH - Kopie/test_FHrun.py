import unittest
from PIL import Image
from run_FH_algorithm import FH_run

from Absolute_Intensity import AbsoluteIntensity
class test_FHRun(unittest.TestCase):
    def setUp(self):
        self.img = Image.open("Images/bsd_l_chicken.jpg")
    def test1(self):
        merge = FH_run(self.img,200,'L', 'Grid', AbsoluteIntensity).step_3()
        self.assertEqual(len(merge),15)


