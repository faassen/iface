from iface import MapKey, MultiMap


class ZopeInterfaceMapKey(MapKey):

    def __init__(self, interface):
        super(ZopeInterfaceMapKey, self).__init__(
            interface, map(ZopeInterfaceMapKey, interface.__bases__))


class CompatibilityAdapterRegistry(object):

    def __init__(self):
        self._map = MultiMap()

    def register(self, required, provided, name, value):
        required = map(ZopeInterfaceMapKey, required)
        self._map[required] = value

    def lookup(self, required, provided, name='', default=None):
        required = map(ZopeInterfaceMapKey, required)
        try:
            return self._map[required]
        except KeyError:
            return None
