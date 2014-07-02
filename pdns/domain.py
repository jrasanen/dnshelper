import collections
from numpy import array_equal
from dns.resolver import Resolver
from records import *

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

class Domain(object):
    def __init__(self, name, nameservers=['8.8.8.8', '4.4.4.4',]):
        super(Domain, self).__init__()
        self.name = unicode(name, 'utf-8').encode('idna')
        self.nameservers = []
        self.a_records = []
        self.mx_records = []
        self.ns_records = []
        self.resolver = Resolver(configure=True)
        self.resolver.nameservers = nameservers
        self.resolve()

    def set_resolver(self, resolver):
        self.resolver = resolver

    def _query(self, rtype):
        answers = self.resolver.query(self.name, rtype)
        return answers

    def _resolve_ns(self):
        if not self.ns_records:
            for rdata in self._query('NS'):
                self.ns_records.append(rdata.target.canonicalize())
        return self.ns_records

    def _resolve_mx(self):
        if not self.mx_records:
            for rdata in  self._query('MX'):
                mx = {
                    'exchange': rdata.exchange,
                    'preference': rdata.preference
                }
                self.mx_records.append(Mx(rdata.exchange, rdata.preference))
        return self.mx_records

    def _resolve_a(self):
        if not self.a_records:
            for rdata in self._query('A'):
                self.a_records.append(rdata.address)
        return self.a_records

    def get_mx(self):
        return self._resolve_mx()

    def resolve(self):
        self._resolve_a()
        self._resolve_ns()
        self._resolve_mx()

        return {
            'name': self.name,
            'records': {
                'a': self.a_records,
                'mx': self.mx_records,
                'ns': self.ns_records,
            },
            'answer': {
                'ns': self.resolver.nameservers
            }
        }

    def __eq__(self, other):
        if not array_equal(self.get_mx(), other.get_mx()):
            return False
        return True



