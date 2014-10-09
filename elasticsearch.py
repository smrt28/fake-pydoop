
class Indices:
    def __init__(self):
        pass

    def exists(self, key):
        return True

class Elasticsearch:
    def __init__(self, p1):
        self.indices = Indices()

    def index(self, **params):
        print "ES_INDEX: %s" % params
