from itertools import cycle
from time import sleep

from streamparse import Spout

class RandomSentenceSpout(Spout):
    outputs = ['word']

    def initialize(self, stormconf, context):
        self.sentences = cycle([
            "the cow jumped over the moon",
            "an apple a day keeps the doctor away",
            "four score and seven years ago",
            "snow white and the seven dwarfs",
            "i am at two with nature"
        ])

    def next_tuple(self):
        sleep(0.1)
        sentence = next(self.sentences)
        self.emit([sentence])
        self.logger.info("- [pid={}] - Emitting: spout [{}]".format(self.pid,sentence))