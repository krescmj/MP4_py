from streamparse import Grouping, Topology

from spouts.FileReaderSpout import FileReaderSpout
from bolts.SplitSentenceBolt import SplitSentenceBolt
from bolts.NormalizerBolt import NormalizerBolt
from bolts.WordCountBolt import WordCountBolt
from bolts.TopNFinderBolt import TopNFinderBolt

class TopWordFinderTopologyPartC(Topology):
    config = {'coursera.datafile': 'resources/data.txt'}

    # TODO:
    # Task: wire up the topology
    # Make sure you use the following names for each component
    # FileReaderSpout -> "spout"
    # SplitSentenceBolt -> "split"
    # WordCountBolt -> "count"
    # NormalizerBolt -> "normalize"
    # TopNFinderBolt -> "top-n"


    # NOTE: will have to manually kill Topology after submission
    sentence_spout = FileReaderSpout.spec(name='spout')
    split_bolt = SplitSentenceBolt.spec(name='split', inputs=[sentence_spout])
    normalize_bolt = NormalizerBolt.spec(name='normalize', inputs=[split_bolt])
    count_bolt = WordCountBolt.spec(name='count', inputs={normalize_bolt: Grouping.fields('word')})
    topnfinder_bolt = TopNFinderBolt.spec(name='top-n', inputs={count_bolt: Grouping.fields('word')})
