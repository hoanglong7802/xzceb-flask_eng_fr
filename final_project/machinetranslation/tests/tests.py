import unittest
from ..machinetranslation import translator

class TranslatorTests(unittest.TestCase):

    def testEnglishToFrench1(self):
        translation = translator.englishToFrench('Hello')
        self.assertEqual(translation, 'Bonjour')

    def testFrenchToEnglish1(self):
        translation = translator.frenchToEnglish('Bonjour')
        self.assertEqual(translation, 'Hello')

    def testEnglishToFrench2(self):
        translation = translator.englishToFrench('Student')
        self.assertEqual(translation, 'Étudiant(e)')

    def testFrenchToEnglish2(self):
        translation = translator.frenchToEnglish('Étudiant(e)')
        self.assertEqual(translation, 'Student')

if __name__ == '__main__':
    unittest.main()