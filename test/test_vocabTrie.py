import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from vocabtrie import VocabTrie
import kenlm

class TestVocabTrie(unittest.TestCase):
    def setUp(self):
        self.vocabtrie = VocabTrie()
        self.language_model = kenlm.LanguageModel('../resources/lm_word_medium.kenlm')

    def test_add_word(self):
        self.vocabtrie.add_word('abc')
        #self.fail()


    def test_get_words_with_prefix(self):
        self.vocabtrie.add_word('abc')
        stateIn = kenlm.State()
        stateOut = kenlm.State()
        words_with_probs = self.vocabtrie.get_words_with_prefix('a', self.language_model, stateIn, stateOut).pop(0)
        self.assertEqual(words_with_probs[0], 'abc', 'Returned item is not equal')



if __name__ == '__main__':
    unittest.main()

