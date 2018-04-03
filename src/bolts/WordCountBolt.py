from collections import Counter

from streamparse import Bolt

class WordCountBolt(Bolt):
    outputs = ['word', 'count']

    def initialize(self, storm_conf, context):
        self.counter = Counter()

    def process(self, tup):
        word = tup.values[0]
        # TODO:
        # use the "self.logger.info(...)" function to print 1. the message received and 2. the message emitted
        self.logger.info("- [pid={}] - Processing received message [{}]".format(self.pid,word))
        self.counter[word] += 1
        self.emit([word, self.counter[word]])
        self.logger.info("- [pid={}] - Emitting: count [{},{}]".format(self.pid,word,self.counter[word]))