from pychronic.models.data_types import DataType


class TaggedWord:
    def __init__(self, word: str, datatype: DataType, stemmed_word):
        self.word = word
        self.datatype = datatype
        self.stemmed_word = stemmed_word
