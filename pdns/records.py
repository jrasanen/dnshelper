
class Mx(object):
    def __init__(self, exchange, preference):
        super(Mx, self).__init__()
        self.exchange = exchange
        self.preference = preference

    def mx(self):
        return self.exchange

    def pref(self):
        return self.preference

    def __eq__(self, other):
        return self.mx() == other.mx() and self.pref() == other.pref()

    def __repr__(self):
        return u'<MX {0}, {1}>'.format(self.exchange, self.preference)

    def __unicode__(self):
        return u'{0} {1}'.format(self.exchange, self.preference)

    def __str__(self):
        return '{0} {1}'.format(self.exchange, self.preference)



class A(object):
    def __init__(self, name, address):
        super(A, self).__init__()
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    def __eq__(self, other):
        return self.name() == other.name() and self.address() == other.address()

    def __repr__(self):
        return u'<A {0}, {1}>'.format(self._name, self._address)

    def __unicode__(self):
        return u'{0} {1}'.format(self._name, self._address)

    def __str__(self):
        return '{0} {1}'.format(self._name, self._address)

