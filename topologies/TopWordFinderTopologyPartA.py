from streamparse import Grouping, Topology

from spouts.RandomSentenceSpout import RandomSentenceSpout
from bolts.SplitSentenceBolt import SplitSentenceBolt
from bolts.WordCountBolt import WordCountBolt

class TopWordFinderTopologyPartA(Topology):
    # TODO:
    # Task: wire up the topology
    # Make sure you use the following names for each component
    # RandomSentenceSpout -> "spout"
    # SplitSentenceBolt -> "split"
    # WordCountBolt -> "count"

   
    # NOTE: will have to manually kill Topology after submission
	
	sentence_spout = RandomSentenceSpout.spec(name='spout')
	split_bolt = SplitSentenceBolt.spec(name='split', inputs=[sentence_spout])
	count_bolt = WordCountBolt.spec(name='count', inputs={split_bolt: Grouping})
