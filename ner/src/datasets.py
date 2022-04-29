from flair.data import Corpus
from flair.data_fetcher import NLPTaskDataFetcher 

class NERCorpus:
    def __init__(self, corpus_name) -> None:
        self.corpus_name = corpus_name
        
    def create_corpus(self) -> Corpus:
        corpus = NLPTaskDataFetcher.load_column_corpus(data_folder = '{}/'.format(self.corpus_name), 
                                                column_format = {0: 'text', 1: 'ner'},
                                                train_file = 'train.conll'.format(self.corpus_name),
                                                test_file = 'test.conll'.format(self.corpus_name),
                                                dev_file = 'dev.conll'.format(self.corpus_name)
        )
        return corpus


class TextClassificationCorpus:
    def __init__(self, path) -> None:
        self.path = path