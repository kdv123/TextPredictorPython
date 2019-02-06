import unittest
import kenlm
from predictor import WordPredictor
from vocabtrie import VocabTrie

class TestWordPredictor(unittest.TestCase):

    def setUp(self):
        self.wordPredictor = WordPredictor('resources/lm_word_medium.kenlm', 'resources/vocab_100k')
        self.languageModel = kenlm.LanguageModel('resources/lm_word_medium.kenlm')
        self.vocab_filename = 'vocab_100k'

    def test_create_new_trie(self):
        wp = self.wordPredictor
        self.assertIsInstance(wp.create_new_trie(self.vocab_filename), VocabTrie, "OK")


    def test_add_vocab(self, vocab_id = 'vocab_id'):
        new_trie = self.wordPredictor.create_new_trie(self.vocab_filename)
        self.assertTrue((new_trie!= None))
        self.assertFalse((new_trie == None))

    def test_get_vocab_trie(self):
        flag, vocabTr = self.wordPredictor.get_vocab_trie(vocab_id = 'vocab_100k')
        self.assertIsInstance(vocabTr, VocabTrie, 'OK')
        self.assertTrue(flag, 'True')
        self.assertFalse(flag, 'False')

    def test_get_punc_token(self):
        self.assertEqual(self.wordPredictor.get_punc_token(','), ',comma', 'OK')

    def test_get_context_state(self):
        sIn, sOut = self.wordPredictor.get_context_state('<s>', self.languageModel)
        self.assertIsInstance(sIn, kenlm.State, 'OK')
        self.assertIsInstance(sOut, kenlm.State, 'OK')

    def test_update_char_list_from_string(self):
        self.fail()
    #def test_get_words(self):


    def test__get_words(self):
        self.fail()

    def test_print_suggestions(self):
        self.fail()

    def test_get_most_likely_word(self):
        self.fail()



if __name__ == '__main__':
    unittest.main()
