from streamparse import Bolt

class SplitSentenceBolt(Bolt):
    outputs = ['word']

    def process(self, tup):
        sentence = tup.values[0]
        self.logger.info("- [pid={}] - Processing received message [{}]".format(self.pid,sentence))
        for word in sentence.split():
            self.emit([word])
            self.logger.info("- [pid={}] - Emitting: split [{}]".format(self.pid,word))