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

    fr_spout = FileReaderSpout.spec(name='spout')

    ss_inputs = {
        fr_spout: Grouping.SHUFFLE
    }
    ss_bolt = SplitSentenceBolt.spec(name='split', par=8, inputs=ss_inputs)

    wc_inputs ={
        ss_bolt: Grouping.fields('word')
    }
    wc_bolt = WordCountBolt.spec(name='count', par=12, inputs=wc_inputs)

    # NOTE: will have to manually kill Topology after submission
