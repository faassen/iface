class MapKey(object):
    def __init__(self, key, parents=()):
        self.key = key
        self.parents = parents
        # we need Python's mro, but we don't have classes. We create
        # some with the same structure as our parent structure. then we
        # get the mro
        self._mro_helper = type('fake_type',
                                tuple(parent._mro_helper for
                                      parent in parents),
                                {'mapkey': self})
        # we then store the map keys for the mro (without the last
        # entry, which is always object)
        self._parent_mapkeys = [
            base.mapkey for base in self._mro_helper.__mro__[:-1]]

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self):
        return "<MapKey: %r>" % self.key

class Map(dict):

    # sometimes we want to look up things exactly in the underlying
    # dictionary
    exact_getitem = dict.__getitem__
    exact_get = dict.get
    
    def __getitem__(self, key):
        for mapkey in key._parent_mapkeys:
            try:
                return super(Map, self).__getitem__(mapkey)
            except KeyError:
                pass
        raise KeyError(key)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

class MultiMap(object):
    def __init__(self):
        self._by_arity = {}
        
    def __setitem__(self, key, value):
        arity = MapKey(len(key))
        key = [arity] + list(key)
        last_key = key.pop()
        map = self._by_arity
        for k in key:
           submap = dict(map).get(k)
           if submap is None:
               submap = map[k] = Map()
           map = submap
        map[last_key] = value

    def __delitem__(self, key):
        arity = MapKey(len(key))
        key = [arity] + list(key)
        last_key = key.pop()
        map = self._by_arity
        for k in key:
            map = dict(map)[k]
        del map[last_key]

    def __getitem__(self, key):
        arity = MapKey(len(key))
        map = self._by_arity
        return self._getitem_recursive(map, arity, *key)

    # XXX missing exact_getitem, exact_get

    def _getitem_recursive(self, map, k, *key):
        if not key:
            return map[k]
        for parent in k._parent_mapkeys:
            try:
                return self._getitem_recursive(map[parent], *key)
            except KeyError, e:
                pass
        raise e
