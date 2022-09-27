import sys
from unittest import TestCase, main as unittest_main
from typing import List, Tuple
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

from services.nlp.roberta.roberta import RoBERTa
from services.nlp.bert.bert import BERT


class NlpServiceTester(TestCase):
    roberta_model = RoBERTa(mode='test')
    roberta_model.start()

    bert_model = BERT(mode='test')
    bert_model.start()

    @staticmethod
    def __bert_input_template(data: str) -> dict:
        return {
            "type": "message",
            "pattern": None,
            "channel": "bert_model_input",
            "data": data,
        }

    @staticmethod
    def __roberta_input_template(data: str) -> dict:
        return {
            "type": "message",
            "pattern": None,
            "channel": "roberta_model_input",
            "data": data,
        }

    @classmethod
    def __predict(cls, user_input: str, model="bert") -> Tuple[str, List[str]]:
        """Makes prediction and returns the predicted slots list"""

        if model == "bert":
            input_ = cls.__bert_input_template(user_input)
            prediction = cls.bert_model.predict(input_)
        if model == "roberta":
            input_ = cls.__roberta_input_template(user_input)
            prediction = cls.roberta_model.predict(input_)

        slots = prediction["slots"]
        predicted_label = prediction["intent"]["name"]
        predicted_slots = [slot.get("slot", None) for slot in slots]
        return predicted_label, predicted_slots

    def _nlp_predict_test(self, user_input: str, actual_slots: str, model: str):
        """ Testing BERT and Roberta

        Args:
            user_input: input taken from user
            actual_slots: expected slots
        """
        predicted_label, predicted_slots = self.__predict(user_input, model)
        self.assertListEqual(actual_slots, predicted_slots)


class NlpServiceTest(NlpServiceTester):
    def test_01(self):
        user_input = "Nasilsin"
        actual_slots = ["smalltalk"]
        model = "bert"
        super()._nlp_predict_test(user_input, actual_slots, model)

    def test_02(self):
        user_input = "italya'da sicaklik nedir"
        actual_slots = ["city", "weather_request"]
        model = "bert"
        super()._nlp_predict_test(user_input, actual_slots, model)

    def test_03(self):
        user_input = "bitcoin fiyatı"
        actual_slots = ["question_text"]
        model = "bert"
        super()._nlp_predict_test(user_input, actual_slots, model)

    def test_04(self):
        user_input = "naptin"
        actual_slots = ["smalltalk"]
        model = "roberta"
        super()._nlp_predict_test(user_input, actual_slots, model)

    def test_05(self):
        user_input = "dolar ne kadar"
        actual_slots = ["question_text"]
        model = "roberta"
        super()._nlp_predict_test(user_input, actual_slots, model)

    def test_06(self):
        user_input = "i want to chat"
        actual_slots = ["chat"]
        model = "roberta"
        super()._nlp_predict_test(user_input, actual_slots, model)


if __name__ == '__main__':
    unittest_main()
