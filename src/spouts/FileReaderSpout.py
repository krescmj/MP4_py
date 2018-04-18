import os
from os.path import join
from time import sleep

from streamparse import Spout

class FileReaderSpout(Spout):
    outputs = ['word']
	
    sentences = list()

    def initialize(self, stormconf, context):
        datafile = join(os.getcwd(), stormconf['coursera.datafile'])

        # TODO:
        # Task: Initialize the file reader
		
        self.f = open('datafile', 'r')
		
        for self.line in self.f:
			self.sentences.appened(self.line)
			
        self.f.close()


    def next_tuple(self):
        # TODO:
        # Task 1: read the next line and emit a tuple for it
        # Task 2: don't forget to sleep for 1 second when the file is
        #         entirely read to prevent a busy-loop
        # Task 3: use the "self.logger.info(...)" function to print 1. the message received and 2. the message emitted 

		#sleep(1.0)
        sentence = next(self.sentences)
        self.emit([sentence])
        self.logger.info("- [pid={}] - Emitting: spout [{}]".format(self.pid,sentence))
        sleep(1.0)
		
        #pass

    # NOTE: Streamparse does not have a close() function
    #       Closing the file should be handled in initialize() itself