#!/usr/bin/python

import kenlm  # pip install https://github.com/kdv123/archive/master.zip
import vocabtrie

INF = 2147483647

class WordPredictor:
    wordList = []

    def __init__(self, lm_filename, vocab_filename):
        self.lmFileName = lm_filename
        self.vocab_filename = vocab_filename
        self.language_model = kenlm.LanguageModel(lm_filename)
        #char_list can also be constructed by calling the create_char_list_from_vocab function
        #To create a character list when creating a trie call the above mentioned function
        #from add_vocab function
        self.next_char_li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', "'", '.', ',', '?', '#', '$', '@']
        self.trieTable = {}
        self.add_vocab('', self.vocab_filename)

    # Given a filename, this method creates a new trie data
    # structure for the words in the file
    @staticmethod
    def create_new_trie(vocab_filename):
        word_list = []
        newVocabTrie = vocabtrie.VocabTrie()
        with open(vocab_filename) as fp:
            for line in fp:
                line = line.strip()
                word_list.append(line)
                newVocabTrie.add_word(line)
        return newVocabTrie

    #Function to update character list
    @staticmethod
    def update_char_list_from_string(char_list, string):
        for char in string:
            char_list.append(char)
        return char_list

    #Given a vocab_id and vocab_filename, the following function adds every
    #unique character of the vocabulary in a character list
    @staticmethod
    def create_char_list_from_vocab(vocab_id, vocab_filename):
        char_list = set()
        char_list_by_vocab_id = {}
        with open(vocab_filename) as fp:
            #i = 0
            for line in fp:
                line = line.strip()
                for char in line:
                    char_list.add(char)

        char_list_by_vocab_id[vocab_id] = char_list
        return char_list_by_vocab_id

    @staticmethod
    def get_punc_token(punctuation):
        if punctuation == ',':
            return ',comma'
        elif punctuation == '.':
            return '.period'
        elif punctuation == ',?':
            return '?question-mark'
        elif punctuation == '!':
            return '!exclamation-point'

    # This method adds a vocabulary to the instance of the class. The vocabulary
    # is saved as a Trie data structure. For multiple vocabularies, the Tries are
    # mapped in a hash table with a vocab_id
    # The trie can be accessed by the vocab_id provided
    def add_vocab(self, vocab_id, vocab_filename):
        if self.trieTable.has_key(vocab_id):
            print('Vocabulary with id "' + vocab_id + '" already exists, try a new id.')
            return False
        new_trie = self.create_new_trie(vocab_filename)
        self.trieTable[vocab_id] = new_trie
        print('Vocab added successfully')
        return True

    # Given a vocab_id, this method returns the trie from the trie table that
    # is referenced by the vocab_id
    def get_vocab_trie(self, vocab_id):
        if self.trieTable.has_key(vocab_id):
            return True, self.trieTable[vocab_id]
        else:
            #print('Error! Vocabulary with id "' + vocab_id + ' " has not been found.')
            return False, None



    # This method returns the kenlm states for the given context
    def get_context_state(self, context, model):
        stateIn = kenlm.State()
        stateOut = kenlm.State()
        context = '<s> ' + context
        contextWords = context.split()
        for w in contextWords:
            print('Context', '{0}\t{1}'.format(model.BaseScore(stateIn, w, stateOut), w))
            stateIn = stateOut
            stateOut = kenlm.State()

        return stateIn, stateOut

    def get_words(self, *args):
        num_of_args = len(args)
        prefix = ''
        context = ''
        vocab_id = ''
        num_predictions = 3
        min_log_prob = -INF

        # arguments in the form 'prefix, vocab_id, num_of_predictions, min_log_prob'
        if num_of_args == 4:
            prefix = args[0]
            # print(prefix)
            vocab_id = args[1]
            # print(vocab_id)
            num_predictions = args[2]
            # print(num_of_predictions)
            min_log_prob = args[3]
            # print(min_log_prob)
            return self._get_words(prefix, '', vocab_id, num_predictions, min_log_prob)

        # arguments in the form 'prefix, context, vocab_id, num_of_predictions, min_log_prob'
        elif num_of_args == 5:
            prefix = args[0]
            # print(prefix)
            context = args[1]
            # print(context)
            vocab_id = args[2]
            # print(vocab_id)
            num_of_predictions = args[3]
            # print(num_of_predictions)
            min_log_prob = args[4]
            # print(min_log_prob)
            return self._get_words(prefix, context, vocab_id, num_predictions, min_log_prob)

        else:
            print('Invalid number of arguments')
            return []

    def _get_words(self, prefix, context, vocab_id, num_predictions, min_log_prob):
        (stateIn, stateOut) = self.get_context_state(context, self.language_model)

        flag, currentTrie = self.get_vocab_trie(vocab_id)
        if flag == False:
            return []

        most_prob_word = ''
        most_prob_word_log = min_log_prob

        suggestion_list = []
        for char in self.next_char_li:
            new_prefix = prefix + char
            # print(new_prefix)
            words_with_log_prob = currentTrie.get_words_with_prefix(new_prefix, self.language_model, stateIn, stateOut)

            #Update the most probable word
            most_prob_word, most_prob_word_log = self.find_most_probable_word(words_with_log_prob, most_prob_word, most_prob_word_log)

            #sort the most probable words for this prefix
            likely_words_with_logprob = sorted(words_with_log_prob, key=lambda x: float(x[1]), reverse=True)

            #add the most probable words to the suggestion list for this prefix
            suggestion_list.append(likely_words_with_logprob[:num_predictions])

        # Print the most probable word if needed
        #print('Context: ' + context)
        #print('Prefix: ' + prefix)
        #print('Most likely word: "' + most_prob_word + '" with log probability: ' + str(most_prob_word_log))
        return suggestion_list

    #Input: a list of probable words and their proability for a list of prefix
    #Example: [[0, [['a', -2.04],['aa', -3.04],['ab', -2.04]]], [[1, [['b', -2.04],['ba', -3.04],['bb', -2.04]]] .....]
    def print_suggestions(self, suggestion_list):
        print('--------------------------------------------')
        print('Word\tProbability')
        print('--------------------------------------------')
        for i, word_list in enumerate(suggestion_list):
            for w, p in word_list:
                print('' + w + '\t' + str(p))

    def find_most_probable_word(self, word_list, prob_word, max_log_prob):
        word = prob_word
        log_prob = max_log_prob
        for w, p in word_list:
            if p > log_prob:
                word = w
                log_prob = p
        return word, log_prob

    def get_most_probable_word(self, prefix, context, vocab_id, min_log_prob = -INF):
        (stateIn, stateOut) = self.get_context_state(context, self.language_model)
        most_prob_word = ''
        most_prob_word_log = min_log_prob

        flag, currentTrie = self.get_vocab_trie(vocab_id)
        if flag == False:
            return most_prob_word, most_prob_word_log

        words_with_log_prob = currentTrie.get_words_with_prefix(prefix, self.language_model, stateIn, stateOut)
        # Update the most probable word
        most_prob_word, most_prob_word_log = self.find_most_probable_word(words_with_log_prob, most_prob_word, most_prob_word_log)

        # Print the most probable word if needed
        print('Context: ' + context)
        print('Prefix: ' + prefix)
        print('Most likely word: "' + most_prob_word + '" with log probability: ' + str(most_prob_word_log))

        return most_prob_word, most_prob_word_log


def main():
    lm_filename = 'resources/lm_word_medium.kenlm'
    vocab_filename = 'resources/vocab_100k'
    predictor = WordPredictor(lm_filename, vocab_filename)

    #print(predictor.create_char_list_from_vocab(vocab_filename))

    #words = predictor.get_words('f', '', 3, -inf)
    #predictor.print_suggestions(words)

    words = predictor.get_words('a', 'the united states of', '', 3, -INF)
    predictor.print_suggestions(words)
    #print(predictor.get_most_likely_word(words))
    #predictor.add_vocab('vocab_100k', vocab_filename)

    predictor.get_most_probable_word('a', 'the united states of', '')



if __name__ == "__main__":
    main()

