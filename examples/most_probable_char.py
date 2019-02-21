# This is an example script to run the CharacterPredictor class and get the
# most probable character for a given context.

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from character_predictor import CharacterPredictor




def main():
	lm_filename = '../resources/lm_char_medium.kenlm'
	character_filename = '../resources/char_set.txt'

	char_predictor = CharacterPredictor(lm_filename, character_filename)
	print(char_predictor.get_most_probable_character('the united states of '))



if __name__ == "__main__":
    main()