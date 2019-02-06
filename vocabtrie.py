#!/usr/bin/python


class TrieNode:
    def __init__(self, label=None, data=None):
        self.label = label
        self.data = data
        self.children = dict()
        self.exists = False

    def add_child(self, key, data=None):
        if not isinstance(key, TrieNode):
            self.children[key] = TrieNode(key, data)
        else:
            self.children[key.label] = key

    """def __getitem__(self, key):
        return self.children[key]"""


class VocabTrie(object):
    def __init__(self):
        self.root = TrieNode()

    def __getitem__(self, key):
        return self.root.children[key]

    def add_word(self, word):
        current_node = self.root
        for character in word:
            if character in current_node.children:
                current_node = current_node.children[character]
            else:
                current_node.add_child(character)
                current_node = current_node.children[character]

        current_node.data = word

    def has_word(self, word):
        if not word:
            return False

        current_node = self.root
        exists = True
        for character in word:
            if character in current_node.children:
                current_node = current_node.children[character]
            else:
                exists = False
                break
        if exists:
            if current_node.data == None:
                exists = False

        return exists

    """ Returns a list of all words in tree that start with prefix """

    def get_words_with_prefix(self, prefix, model, stateIn, stateOut):
        words = []
        probabilities = []
        wordsWithProbs = []

        if prefix == None:
            prefix = ''

        # Determine end-of-prefix node
        top_node = self.root
        for character in prefix:
            if character in top_node.children:
                top_node = top_node.children[character]
            else:
                # return words, probabilities
                return wordsWithProbs

        # Get words under prefix
        if top_node == self.root:
            queue = [node for key, node in top_node.children.iteritems()]
        else:
            queue = [top_node]

        # Perform a breadth first search under the prefix
        while queue:
            current_node = queue.pop()
            if current_node.data != None:
                words.append(current_node.data)
                logProb = model.BaseScore(stateIn, current_node.data, stateOut)
                probabilities.append(logProb)
                # wordsWithProbs.append(current_node.data)
                # wordsWithProbs.append(logProb)
                # wordsWithProbs[current_node.data] = logProb
                tup = (current_node.data, logProb)
                wordsWithProbs.append(tup)

            queue = [node for key, node in current_node.children.iteritems()] + queue

        return wordsWithProbs



