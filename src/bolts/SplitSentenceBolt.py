from streamparse import Bolt

class SplitSentenceBolt(Bolt):
    outputs = ['word']

    def process(self, tup):
        sentence = tup.values[0]
        # TODO:
        # use the "self.logger.info(...)" function to print 1. the message received and 2. the message emitted 
        self.logger.info("- [pid={}] - Processing received message [{}]".format(self.pid,sentence))
        for word in sentence.split():
            self.emit([word])
            self.logger.info("- [pid={}] - Emitting: split [{}]".format(self.pid,word))