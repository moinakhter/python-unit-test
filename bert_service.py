import sys
from unittest import TestCase, main as unittest_main
from typing import List, Tuple
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

from services.nlp.bert.bert import BERT


class BertServiceTester(TestCase):
    model = BERT(mode='test')
    model.start()

    @staticmethod
    def __nlp_input_template(data: str) -> dict:
        return {
            "type": "message",
            "pattern": None,
            "channel": "bert_model_input",
            "data": data,
        }

    @classmethod
    def __predict(cls, sentence: str) -> Tuple[str, List[str]]:
        """Makes prediction and returns the predicted slots list"""
        input_ = cls.__nlp_input_template(sentence)
        prediction = cls.model.predict(input_)
        slots = prediction["slots"]
        predicted_label = prediction["intent"]["name"]
        predicted_slots = [slot.get("slot", None) for slot in slots]
        return predicted_label, predicted_slots

    def _bert_predict_test(self, user_input: str, actual_slots: str):
        """ Testing BERT

        Args:
            user_input: input taken from user
            actual_slots: expected slots
            print_result: print response in the console for developer testing.
        """

        redicted_label, predicted_slots = self.__predict(user_input)
        self.assertListEqual(actual_slots, predicted_slots)


class BertTest(BertServiceTester):

    def test_01(self):
        user_input = "Nasilsin"
        actual_slots = ["smalltalk"]
        super()._bert_predict_test(user_input, actual_slots)

    def test_02(self):
        user_input = "hava sıcaklığı"
        actual_slots = ["weather_request"]
        super()._bert_predict_test(user_input, actual_slots)

    def test_03(self):
        user_input = "dolar fiyatı"
        actual_slots = ["question_text"]
        super()._bert_predict_test(user_input, actual_slots)

    def test_04(self):
        user_input = "bitcoin fiyatı"
        actual_slots = ["question_text"]
        super()._bert_predict_test(user_input, actual_slots)

    def test_05(self):
        user_input = "bugün nasil hissediyorsun"
        actual_slots = ["smalltalk"]
        super()._bert_predict_test(user_input, actual_slots)

    def test_06(self):
        user_input = "espri yap"
        actual_slots = ["tell_me"]
        super()._bert_predict_test(user_input, actual_slots)

    def test_07(self):
        user_input = "kizgin misin"
        actual_slots = ["ask_angry"]
        super()._bert_predict_test(user_input, actual_slots)

    def test_08(self):
        user_input = "italya'da sicaklik nedir"
        actual_slots = ["city", "weather_request"]
        super()._bert_predict_test(user_input, actual_slots)

    def test_09(self):
        user_input = "çok iyisin"
        actual_slots = ["compliment"]
        super()._bert_predict_test(user_input, actual_slots)


if __name__ == '__main__':
    unittest_main()
