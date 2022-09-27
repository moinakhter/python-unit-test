import sys
from unittest import TestCase, main as unittest_main
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

from services.translation.translate import Translate


class TranslationServiceTester(TestCase):
    translator = Translate()

    def __assert_interaction(self, response: str, expected: str) -> None:
        """ Testing response and expected text are correct or not.

        Args:
            response: Translation result
            expected: Translation expected result
        """
        self.assertEqual(response, expected)

    def _online_translate(self, sentence: str, expected_result: str, target_language="tr", print_result=False):
        """ Testing Online Translation

        Args:
            sentence: Sentence which need to translate from online
            expected_result: Online translation response
            target_language: Translation language 
            print_result: print translation response in the console for developer testing.
        """
        trans_response = self.translator.translate(sentence, target_language)[0]
        if print_result:
            print("\033[94m Online Translation Response: " + trans_response)
        self.__assert_interaction(trans_response, expected_result)

    def _offline_translate(self, sentence: str, expected_result: str, target_language="tr", print_result=False):
        """ Testing Offline Translation

        Args:
            sentence: Sentence which need to translate from online
            expected_result: Online translation response
            target_language: Translation language, for offline testing we are translating sentences only for English and Turkish.
            print_result: print translation response in the console for developer testing.
        """
        trans_response = Translate.offline(sentence, target_language)
        if print_result:
            print("\033[94m Offline Translation Response: " + trans_response)
        self.__assert_interaction(trans_response, expected_result)


class OnlineTranslationTest(TranslationServiceTester):

    def test_01(self):
        sentence = "nasilsiniz"
        expected_result = "how are you "
        language = "en"
        self._online_translate(sentence, expected_result, language, True)

    def test_02(self):
        sentence = "nasilsiniz"
        expected_result = "آپ کیسے ہو "
        language = "ur"
        self._online_translate(sentence, expected_result, language)

    def test_03(self):
        sentence = "nasilsiniz"
        expected_result = "cómo estás "
        language = "es"
        self._online_translate(sentence, expected_result, language)


class OfflineTranslationTest(TranslationServiceTester):

    def test_01(self):
        sentence = "nasilsiniz"
        expected_result = "How are you?"
        self._offline_translate(sentence, expected_result, target_language="en", print_result=True)

    def test_02(self):
        sentence = "kimdir"
        expected_result = "Who is it?"
        self._offline_translate(sentence, expected_result, target_language="en")

    def test_03(self):
        expected_result = "Nasılsın?"
        sentence = "How are you?"
        self._offline_translate(sentence, expected_result, target_language="tr")

    def test_04(self):
        expected_result = "Kim o?"
        sentence = "Who is it?"
        self._offline_translate(sentence, expected_result, target_language="tr")


if __name__ == '__main__':
    unittest_main()
