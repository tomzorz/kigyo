# protip: collections.abc -> abstract base classes to inherit from

from collections.abc import Sequence
from itertools import chain

class SampleCollection(Sequence):

    def __init__(self, items = None):
        self._items = items if items is not None else []

    # container protocol

    # for "in" and "not in" operators

    def __contains__(self, item):
        return item in self._items

    # sized protocol

    # for "len" operator

    def __len__(self):
        return len(self._items)

    # iterable protocol

    # for "iter" operator

    def __iter__(self):
        return iter(self._items)

    # sequence protocol

    # for indexing, slicing and more...

    def __getitem__(self, index):
        # we could get a slice here or an int here
        result = self._items[index]
        return SampleCollection(result) if isinstance(index, slice) else result

    # python collections typically overwrite equality operators

    def __eq__(self, other):
        if not isinstance(other, SampleCollection):
            return NotImplemented # important, we return not raise
        return self._items == other._items

    # python is smart and figures out not equal for us, but it's still strongly recommended to override that too if we override eq

    def __ne__(self, other):
        if not isinstance(other, SampleCollection):
            return NotImplemented
        return self._items != other._items

    # now back to sequence

    # dunder reversed would be used, but if it doesn't exist python will do with dunder getitem and dunder len

    # for "index" and "count" operator
    # we can just inherit from Sequence

    # for concatenation and repetition

    def __add__(self, other):
        # noinspection PyProtectedMember
        return SampleCollection(chain(self._items, other._items))

    def __mul__(self, other):
        # this is probably incorrect here
        return self if other > 0 else SampleCollection()

    def __rmul__(self, other):
        return self * other

    # set protocol

    # ... skip as we didn't base it on