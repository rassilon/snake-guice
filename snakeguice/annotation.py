class Annotation(object):
    """Base class for all annotations."""

    def __init__(self, value):
        self._value = str(value)

    def __hash__(self):
        return hash(self.__class__.__name__ + ":" + self._value)

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__ \
               and self._value == other._value

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "<Annotation class '%s' value: %s>" % (self.__class__.__name__, self._value)
