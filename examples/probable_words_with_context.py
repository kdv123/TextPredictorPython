#!/usr/bin/python

# This is an example script to run the WordPredictor class and get
# a list of words that begins with the prefix and a each of the valid 
# character in the character list appened to it. For example, given
# a prefix 'a' and if the chracters in the vocabulary are [a,b,c], it 
# will return a list of words that begin with 'aa', 'ab' and 'ac'.

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from predictor import WordPredictor


def main():
	# Provide the name and path of a language model and the vocabulary
	lm_filename = '../resources/lm_word_medium.kenlm'
	vocab_filename = '../resources/vocab_100k'

	# Create an instance of the WordPredictor class
	word_predictor = WordPredictor(lm_filename, vocab_filename)

	prefix = 'a'
	context = 'the united states of'

	# Define how many predictions you want for each character
	# By default it is set to 0 and will return all possible 
	# words
	num_predictions = 3
	min_log_prob = -float('inf')

	#The default vocab_id is ''
	vocab_id = ''

	word_list = word_predictor.get_words_with_context(prefix, context, vocab_id, num_predictions, min_log_prob)

	# Call the print_suggestions method to print all the words
	word_predictor.print_suggestions(word_list)




if __name__ == "__main__":
    main()