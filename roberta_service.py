import sys
from unittest import TestCase, main as unittest_main
from typing import List, Tuple
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

from services.nlp.roberta.roberta import RoBERTa


class RobertaServiceTester(TestCase):
    model = RoBERTa(mode='test')
    model.start()

    @staticmethod
    def __nlp_input_template(data: str) -> dict:
        return {
            "type": "message",
            "pattern": None,
            "channel": "roberta_model_input",
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

    def roberta_predict_test(self, user_input: str, actual_slots: str):
        """ Testing Roberta

        Args:
            user_input: input taken from user
            actual_slots: expected slots
            print_result: print response in the console for developer testing.
        """
        predicted_label, predicted_slots = self.__predict(user_input)
        self.assertListEqual(actual_slots, predicted_slots)


class RobertaTest(RobertaServiceTester):

    def test_01(self):
        user_input = "how are you"
        actual_slots = ["smalltalk"]
        super().roberta_predict_test(user_input, actual_slots)

    def test_02(self):
        user_input = "nasil cidiyor"
        actual_slots = ["smalltalk"]
        super().roberta_predict_test(user_input, actual_slots)

    def test_03(self):
        user_input = "naptin"
        actual_slots = ["smalltalk"]
        super().roberta_predict_test(user_input, actual_slots)

    def test_04(self):
        user_input = "dolar ne kadar"
        actual_slots = ["question_text"]
        super().roberta_predict_test(user_input, actual_slots)

    def test_05(self):
        user_input = "i want to chat"
        actual_slots = ["chat"]
        super().roberta_predict_test(user_input, actual_slots)


if __name__ == '__main__':
    unittest_main()
