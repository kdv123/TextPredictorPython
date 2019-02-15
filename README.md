# WordPredictor
Library for performing word and chracter level predictions, with the help of kenlm (Language model inference code by Kenneth Heafield, kenlm at kheafield.com).


## System requirements
1. pip
2. Python 2.7
3. kenlm

## Installation
Use the package manager pip to install kenlm 

```bash
pip install https://github.com/kdv123/kenlm/archive/master.zip
```
## Examples
Check the [/examples](https://github.com/sworborno/word_predictor/tree/master/examples) directory under the root repository for some example scripts.
1. [Find most probable word for given context](https://github.com/sworborno/word_predictor/blob/master/examples/most_probable_word.py)
2. [Find a list of probable words for a given prefix and a context](https://github.com/sworborno/word_predictor/blob/master/examples/probable_words_with_context.py)
3. [Add a new vocabulary](https://github.com/sworborno/word_predictor/blob/master/examples/add_vocab_query.py)


## Usage
There are three python scripts which represent three class for the predictor. The [predictor.py](https://github.com/sworborno/word_predictor/blob/master/predictor.py) script contains the WordPredictor 
class and the [chracter_predictor.py](https://github.com/sworborno/word_predictor/blob/master/character_predictor.py) script contains the CharacterPredictor class. The [vocabtrie.py](https://github.com/sworborno/word_predictor/blob/master/vocabtrie.py) contains a VocabTrie class which
is used by the WordPredictor class to create a trie data structure.

To use the WordPredictor class you need to do the following:
```python
from predictor import WordPredictor
```
Then you need to specify the path to a language model filename and a vocabulary filename.
There are some example language models and vocabulary filename in the [resources](https://github.com/sworborno/word_predictor/tree/master/resources)
sub-directory. 

```python
lm_filename = 'resources/lm_char_medium.kenlm'
vocab_filename = 'resources/vocab_100k'
word_predictor = WordPredictor(lm_filename, vocab_filename)
```



