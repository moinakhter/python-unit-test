import threading, sys
from PIL import Image
from numpy import asarray
from os.path import abspath, dirname, join
from unittest import TestCase, main as unittest_main

ASSISTANT_PATH = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, ASSISTANT_PATH)

from services.face_recognizer.pipeline import detection


class FacialRecognitionServiceTester(TestCase):
    def __assert_interaction(self, status: bool) -> None:
        """ Testing Facial Recognition status
        Args:
            status: True or False, True: face detection is working fine. False: not working
        """
        self.assertTrue(status)

    def _face_detection_test(self, image_detection_no=1):
        """ Face Detection
        Args:
            image_detection_no: 1: first user image,
                                2:second user image,
                                3: unknown if user doesn't exist but detection is working fine.
        """
        if image_detection_no == 1:
            img_path = Image.open(ASSISTANT_PATH + '/services/face_recognizer/face_encoder/dataset/Moin_Akhtar/2022-04-26 08-05-30.png')
        elif image_detection_no == 2:
            img_path = Image.open(ASSISTANT_PATH + '/services/face_recognizer/face_encoder/dataset/Majed_Bawarshi/2021-10-05-173211.jpg')
        elif image_detection_no == 3:
            img_path = Image.open(ASSISTANT_PATH + '/services/face_recognizer/face_encoder/dataset/ronaldo.jpeg')
        frame = asarray(img_path)
        result = detection(frame_queue=frame, detection_queue=True, stop_flag=True, nlp_lock=threading.Lock(),
                           mode="test")
        if (result == "Moin_Akhtar" and image_detection_no == 1) or (
                result == "Majed_Bawarshi" and image_detection_no == 2) or (
                result == "unknown" and image_detection_no == 3):
            status = True
        else:
            status = False
        print("\033[92m Face Recognition Result: "+result)
        self.__assert_interaction(status)


class FacialRecognitionTest(FacialRecognitionServiceTester):

    def test_01(self):
        super()._face_detection_test()

    def test_02(self):
        super()._face_detection_test(image_detection_no=2)

    def test_03(self):
        super()._face_detection_test(image_detection_no=3)


if __name__ == '__main__':
    unittest_main()
