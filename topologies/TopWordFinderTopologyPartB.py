from streamparse import Grouping, Topology

from spouts.FileReaderSpout import FileReaderSpout
from bolts.SplitSentenceBolt import SplitSentenceBolt
from bolts.WordCountBolt import WordCountBolt

class TopWordFinderTopologyPartA(Topology):
    config = {'coursera.datafile': 'resources/data.txt'}

    # TODO:
    # Task: wire up the topology
    # Make sure you use the following names for each component
    # FileReaderSpout -> "spout"
    # SplitSentenceBolt -> "split"
    # WordCountBolt -> "count"

    

    # NOTE: will have to manually kill Topology after submission
	
    sentence_spout = FileReaderSpout.spec(name='spout')
    split_bolt = SplitSentenceBolt.spec(name='split', inputs=[sentence_spout])
    count_bolt = WordCountBolt.spec(name='count', inputs={split_bolt: Grouping.fields('word')})
