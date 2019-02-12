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

	# ******The token file is in '../resources/tokens.txt'
	# If you are running this script, then change the token file path in WordPredictor __init__


	# Create an instance of the WordPredictor class
	word_predictor = WordPredictor(lm_filename, vocab_filename)

	# Perform a query with the current vocabulary
	w , p = word_predictor.get_most_probable_word(prefix = 'w', context = 'hello', vocab_id = '', min_log_prob = -float('inf'))

	print('Word: ' + w + ', log probability: ' + str(p))


	new_vocab_filename = '../resources/vocab_20k'
	new_vocab_id = 'small'
	word_predictor.add_vocab(new_vocab_id, new_vocab_filename)

	# Perform a query with the new vocabulary
	w , p = word_predictor.get_most_probable_word(prefix = 'w', context = 'hello', vocab_id = new_vocab_id, min_log_prob = -float('inf'))
	print('Word: ' + w + ', log probability: ' + str(p))


	words = word_predictor.get_words_with_context('w', 'hello', new_vocab_id, 3, -float('inf'))
	word_predictor.print_suggestions(words)


if __name__ == "__main__":
    main()