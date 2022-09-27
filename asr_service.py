import sys
import contextlib
import wave
from os.path import abspath, dirname, join
from unittest import TestCase, main as unittest_main

ASSISTANT_PATH = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, ASSISTANT_PATH)

from services.asr.asr_initializer import ASRRunner


class ASRServiceTester(TestCase):

    def _asr_test(self, wav_path: str) -> None:
        """get the text from the audio file and match similarity of awake word"""
        with contextlib.closing(wave.open(wav_path,
                                          'rb')) as wav_file:
            pcm_data = str(wav_file.readframes(wav_file.getnframes()))

        audio = {'data': pcm_data}
        is_awake_word_matched = ASRRunner.execute_ww(audio, mode="test")
        print(f"\033[92m Result: {is_awake_word_matched}")
        self.__interaction_assert(result=is_awake_word_matched)

    def __interaction_assert(self, result: bool) -> None:
        """ Testing ASR

        Args:
            result: status of awake_word
        """
        self.assertTrue(result)


class ASRTest(ASRServiceTester):
    ww_test_data_path = ASSISTANT_PATH + "/resources/media/test_inputs/wake_word/"

    def test_01(self):
        wav_path = self.ww_test_data_path + "dizzy.wav"
        super()._asr_test(wav_path)

    def test_02(self):
        wav_path = self.ww_test_data_path + "dizzy1.wav"
        super()._asr_test(wav_path)

    def test_03(self):
        wav_path = self.ww_test_data_path + "dizzy2.wav"
        super()._asr_test(wav_path)

    def test_04(self):
        wav_path = self.ww_test_data_path + "dizzy3.wav"
        super()._asr_test(wav_path)

    def test_05(self):
        wav_path = self.ww_test_data_path + "dizzy4.wav"
        super()._asr_test(wav_path)

    def test_06(self):
        wav_path = self.ww_test_data_path + "dizzy5.wav"
        super()._asr_test(wav_path)


if __name__ == '__main__':
    unittest_main()
