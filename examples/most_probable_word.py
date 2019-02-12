#!/usr/bin/python

# This is an example script to run the WordPredictor class and get the
# most probable word given a prefix and a context.

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from predictor import WordPredictor


def main():

	# We need to provide the name and path of a language model
	# and the vocabulary

	lm_filename = '../resources/lm_word_medium.kenlm'
	vocab_filename = '../resources/vocab_100k'

	# Create an instance of the WordPredictor class
	word_predictor = WordPredictor(lm_filename, vocab_filename)

	# The WordPredictor class creates a Trie data structure 
	# for the given vocabulary with a vocab_id. By default
	# the vocab_id is set to ''. If you want to add another 
	# vocabulary then you need to call add_vocab method which 
	# is illustrated in add_vocab_query.py

	# Suppose, we have a prefix 'a' and a context 'the united
	# states of america'. Based on the given information, if 
	# we want to guess the most probable word, then we need
	# to do it following way:


	prefix = 'a'
	context = 'the united states of'
	most_prob_word, log_prob = word_predictor.get_most_probable_word(prefix, context, vocab_id = '', min_log_prob = -float('inf'))

	print('Context: ' + context)
	print('Prefix: ' + prefix)
	print('Most probable word: "' + most_prob_word + '" with log probability: ' + str(log_prob))


	# Another example
	prefix = 'w'
	context = 'hello'
	most_prob_word, log_prob = word_predictor.get_most_probable_word(prefix, context, vocab_id = '', min_log_prob = -float('inf'))

	print('Context: ' + context)
	print('Prefix: ' + prefix)
	print('Most probable word: "' + most_prob_word + '" with log probability: ' + str(log_prob))


if __name__ == "__main__":
    main()