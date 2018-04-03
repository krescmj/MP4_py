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

    rs_spout = RandomSentenceSpout.spec(name='spout', par=5)

    ss_inputs = {
        rs_spout: Grouping.SHUFFLE
    }
    ss_bolt = SplitSentenceBolt.spec(name='split', par=8, inputs=ss_inputs)

    wc_inputs ={
        ss_bolt: Grouping.fields('word')
    }
    wc_bolt = WordCountBolt.spec(name='count', par=12, inputs=wc_inputs)

    # NOTE: will have to manually kill Topology after submission
