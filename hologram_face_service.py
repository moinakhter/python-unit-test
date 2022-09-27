import os, sys, urllib.request
import time
import urllib.request
from os.path import abspath, dirname, join
from unittest import TestCase, main as unittest_main
ASSISTANT_PATH = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, ASSISTANT_PATH)
from helpers.config_helper import ConfigurationHelper


class HologramServiceTester(TestCase):
    __assistant_face_config = ConfigurationHelper.get_conf("assistant_face")
    __hologram_service_script_path = ASSISTANT_PATH + "/services/hologram_face/__main__.py"
    __hologram_url = "http://{0}:{1}".format(__assistant_face_config.get("ip"), __assistant_face_config.get("port"))

    @classmethod
    def __hologram_server_process(cls):
        os.system(ASSISTANT_PATH + f"/.venv/bin/python {cls.__hologram_service_script_path} &")
        time.sleep(3)

    @classmethod
    def __hologram_server_response(cls):
        return urllib.request.urlopen(cls.__hologram_url).getcode()

    @classmethod
    def __hologram_server_process_kill(cls):
        os.system(f"pkill -9 -f {cls.__hologram_service_script_path}")

    @classmethod
    def _hologram_server_test(cls):
        """ Testing Hologram"""
        cls.__hologram_server_process()
        status_code = cls.__hologram_server_response()
        status = status_code == 200
        cls.__hologram_server_process_kill()
        cls.assertTrue(status, "Hologram Server is not working")


class HologramTest(HologramServiceTester):
    def test_01(self):
        super()._hologram_server_test()


if __name__ == '__main__':
    unittest_main()
