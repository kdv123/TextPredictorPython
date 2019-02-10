import unittest
import kenlm
from predictor import WordPredictor
from vocabtrie import VocabTrie
import numbers


class TestWordPredictor(unittest.TestCase):

    def setUp(self):
        self.wordPredictor = WordPredictor('../resources/lm_word_medium.kenlm', '../resources/vocab_100k')
        self.language_model = kenlm.LanguageModel('../resources/lm_word_medium.kenlm')
        self.vocab_filename = '../resources/vocab_100k'
        self.vocab_id = ''

    def test_create_new_trie(self):
        wp = self.wordPredictor
        self.assertIsInstance(wp.create_new_trie(self.vocab_filename), VocabTrie, "OK")

    def test_update_char_list_from_string(self):
        list = ['a']
        str = "bc"
        res = ['a', 'b', 'c']
        self.assertEqual(self.wordPredictor.update_char_list_from_string(list, str), res, "OK")

    def test_create_char_list_from_vocab(self):
        test_res = self.wordPredictor.create_char_list_from_vocab(self.vocab_id, self.vocab_filename)
        id, char_set = test_res.popitem()
        self.assertIsInstance(type(id), type(str), "Return type is not same")
        #self.assertEqual(char_set, type(set), "OK")

    def test_add_vocab(self, vocab_id = 'vocab_id'):
        new_trie = self.wordPredictor.create_new_trie(self.vocab_filename)
        self.assertTrue((new_trie!= None))
        self.assertFalse((new_trie == None))

    def test_get_vocab_trie(self):
        flag, vocabTr = self.wordPredictor.get_vocab_trie(self.vocab_id)
        self.assertIsInstance(vocabTr, VocabTrie, 'Not OK')
        self.assertIsInstance(type(flag), type(bool), "Not OK")


    def test_get_punc_token(self):
        self.assertEqual(self.wordPredictor.get_punc_token(','), ',comma', 'Punctuation and token are not equal')

    def test_get_context_state(self):
        sIn, sOut = self.wordPredictor.get_context_state('<s>', self.language_model)
        self.assertIsInstance(sIn, kenlm.State, 'stateIn is not an instance of kenlm.State')
        self.assertIsInstance(sOut, kenlm.State, 'stateOut is not an instance of kenlm.State')

    def test_find_most_probable_word(self):
        pass

    def test_get_words(self):
        pass

    def test__get_words(self):

        suggestion_list = self.wordPredictor._get_words('a', 'the united states of', self.vocab_id, 3,-float('inf'))
        self.assertTrue(isinstance(type(suggestion_list), type(str)), "Not a list") #basestring is gone in python 3


    def test_print_suggestions(self):
        pass

    def test_get_most_likely_word(self):
        word, log_prob = self.wordPredictor.get_most_probable_word('a', 'the united states of', self.vocab_id)
        self.assertEqual(word, 'america', "Not equal")
        self.assertTrue(isinstance(log_prob, numbers.Number), "False")



if __name__ == '__main__':
    unittest.main()
