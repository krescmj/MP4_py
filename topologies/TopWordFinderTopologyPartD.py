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

    fr_spout = FileReaderSpout.spec(name='spout')

    ss_inputs = {
        fr_spout: Grouping.SHUFFLE
    }
    ss_bolt = SplitSentenceBolt.spec(name='split', par=8, inputs=ss_inputs)

    norm_inputs = {
        ss_bolt: Grouping.SHUFFLE
    }
    norm_bolt = NormalizerBolt.spec(name='normalize', par=8, inputs=norm_inputs)

    wc_inputs = {
        norm_bolt: Grouping.fields('word')
    }
    wc_bolt = WordCountBolt.spec(name='count', par=12, inputs=wc_inputs)

    tnf_inputs = {
        wc_bolt: Grouping.SHUFFLE
    }
    tnf_bolt = TopNFinderBolt.spec(name='top-n', par=1, inputs=tnf_inputs)

    # NOTE: will have to manually kill Topology after submission
