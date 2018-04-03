from streamparse import Bolt

class NormalizerBolt(Bolt):
    outputs = ['word']

    def initialize(self, storm_conf, context):
        self.common_words = [
            "the", "be", "a", "an", "and", "of", "to", "in", "am",
            "is", "are", "at", "not", "that", "have", "i", "it",
            "for", "on", "with", "he", "she", "as", "you", "do",
            "this", "but", "his", "by", "from", "they", "we", "her",
            "or", "will", "my", "one", "all", "s", "if", "any", "our",
            "may", "your", "these", "d" , " ", "me" , "so" , "what" , "him"
        ]

    def process(self, tup):
        # TODO:
        # Task 1: make the words all lower case
        # Task 2: remove the common words

        word = tup.values[0]
        if word:
            word = word.lower()
            if word not in self.common_words:
                self.emit([word])
