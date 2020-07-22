import pickle as cPickle
import pickle
from treys import Card, Evaluator
from treys.lookup import LookupTable

class StrToBytes:
    def __init__(self, fileobj):
        self.fileobj = fileobj
    def read(self, size):
        return self.fileobj.read(size).encode()
    def readline(self, size=-1):
        return self.fileobj.readline(size).encode()


FRONT_LOOKUP = pickle.load(StrToBytes(open("res/front_lookup.p")))


class OFCEvaluator(Evaluator):
    """deuces' evaluator class extended to score an OFC Front."""
    def __init__(self):
        self.table = LookupTable()

        self.hand_size_map = {
            3: self._three,
            5: self._five,
            6: self._six,
            7: self._seven
        }

    def _three(self, cards):
        prime = Card.prime_product_from_hand(cards)
        return FRONT_LOOKUP[prime]
