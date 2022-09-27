import sys
from unittest import TestCase, main as unittest_main
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

from services.question_answering.inference import infer


class QuestionAnswerServiceTester(TestCase):
    def __assert_interaction(self, response: str, expected: str) -> None:
        """ Testing response and expected text are correct or not.

        Args:
            response: Answer of the question
            expected: expected answer
        """
        self.assertEqual(response, expected)

    def _answer_test(self, question: str, corpus: str, expected_result: str, print_result=False):
        """ Testing Question & Answer

        Args:
            question: Question taken from user
            corpus: Text for searching answer from the paragraph
            expected_result: expected answer
            print_result: print response in the console for developer testing.
        """
        infer_response = infer(question, corpus)
        if print_result:
            print("\033[94m Question & Answer Response: " + infer_response[0])
        self.__assert_interaction(infer_response[0], expected_result)


class QuestionAnswerTest(QuestionAnswerServiceTester):

    def test_01(self):
        question = "Recep Tayyip Erdoğan kimdir?"
        corpus = "Recep Tayyip Erdoğan, Türk siyasetçi, Adalet ve Kalkınma Partisi'nin genel başkanı, Türkiye'nin 12. ve günümüzdeki cumhurbaşkanıdır. 2003-2014 yılları arasında 11 yıl Türkiye başbakanlığı yapan Erdoğan, iki dönemdir Türkiye cumhurbaşkanlığı görevini sürdürmektedir."
        expected_result = "Türk siyasetçi, Adalet ve Kalkınma Partisi'nin genel başkanı"
        super()._answer_test(question, corpus, expected_result, True)

    def test_02(self):
        question = "2003-2014 yılları arasında Türkiye'nin başbakanı kimdi?"
        corpus = "Recep Tayyip Erdoğan, Türk siyasetçi, Adalet ve Kalkınma Partisi'nin genel başkanı, Türkiye'nin 12. ve günümüzdeki cumhurbaşkanıdır. 2003-2014 yılları arasında 11 yıl Türkiye başbakanlığı yapan Erdoğan, iki dönemdir Türkiye cumhurbaşkanlığı görevini sürdürmektedir."
        expected_result = "Recep Tayyip Erdoğan"
        super()._answer_test(question, corpus, expected_result)

    def test_03(self):
        question = "İmran Han kimdir?"
        corpus = "İmran Han, Pakistanlı siyasetçi, eski kriket oyuncusu, hayırsever, kriket oyunu yorumcusu ve Bradford Üniversitesi'nin eski rektörü. Ayrıca Han, annesi Şevket Hanım Anısına Kanser Hastanesinin ve Mianvali'de Namal Kolejinin kurucusudur. Han 20. yüzyılın son yirmi yılında ulusal kriket oyuncusuydu."
        expected_result = "Pakistanlı siyasetçi"
        super()._answer_test(question, corpus, expected_result)

    def test_04(self):
        question = "kanser hastanesinin kurucusu kimdir?"
        corpus = "İmran Han, Pakistanlı siyasetçi, eski kriket oyuncusu, hayırsever, kriket oyunu yorumcusu ve Bradford Üniversitesi'nin eski rektörü. Ayrıca Han, annesi Şevket Hanım Anısına Kanser Hastanesinin ve Mianvali'de Namal Kolejinin kurucusudur. Han 20. yüzyılın son yirmi yılında ulusal kriket oyuncusuydu."
        expected_result = "İmran Han"
        super()._answer_test(question, corpus, expected_result)

    def test_05(self):
        question = "İmran Han'ın annesi kimdir?"
        corpus = "İmran Han, Pakistanlı siyasetçi, eski kriket oyuncusu, hayırsever, kriket oyunu yorumcusu ve Bradford Üniversitesi'nin eski rektörü. Ayrıca Han, annesi Şevket Hanım Anısına Kanser Hastanesinin ve Mianvali'de Namal Kolejinin kurucusudur. Han 20. yüzyılın son yirmi yılında ulusal kriket oyuncusuydu."
        expected_result = "Şevket Hanım"
        super()._answer_test(question, corpus, expected_result)

    def test_06(self):
        question = "Türkiye hangi ülkelerle çevrilidir?"
        corpus = "Turkey, or officially the Republic of Turkey, is a country with most of its territory in Anatolia and a small part in Thrace, the southeastern extension of the Balkan Peninsula. It is bordered by Bulgaria in the northwest, Greece in the west, Georgia in the northeast, Armenia, Iran and Azerbaijan in the east, Nakhchivan, and Iraq and Syria in the southeast. It is surrounded by the island of Cyprus and the Mediterranean in the south, the Aegean Sea in the west and the Black Sea in the north. The Sea of Marmara, along with the Bosphorus and the Dardanelles, separates Anatolia from Thrace, that is, Asia from Europe. Turkey has an important geostrategic power as it is located at the crossroads of the European and Asian continents."
        expected_result = "Europe"
        super()._answer_test(question, corpus, expected_result)


if __name__ == '__main__':
    unittest_main()
