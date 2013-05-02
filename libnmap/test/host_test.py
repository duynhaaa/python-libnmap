#!/usr/bin/env python

import unittest
from libnmap import NmapParser

host1 = """
<host starttime="1361738377" endtime="1361738377">
<status state="up" reason="localhost-response"/>
<address addr="127.0.0.1" addrtype="ipv4"/>
<hostnames>
<hostname name="localhost" type="user"/>
<hostname name="localhost" type="PTR"/>
</hostnames>
<ports><extraports state="WILLY_WONCKA" count="995">
<extrareasons reason="conn-refused" count="995"/>
</extraports>
<port protocol="tcp" portid="22">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="ssh" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="25">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="smtp" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="111">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="rpcbind" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="631">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="ipp" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="3306">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="mysql" method="table" conf="3"/>
</port>
</ports>
<times srtt="2100" rttvar="688" to="100000"/>
</host>
"""
host2 = """
<host starttime="1361738318" endtime="13617386177">
<status state="up" reason="localhost-respoe"/>
<address addr="127.0.0.1" addrtype="ipv4"/>
<hostnames>
<hostname name="localhost" type="user"/>
<hostname name="localhost" type="PTR"/>
<hostname name="localhost2" type="PTR"/>
</hostnames>
<ports><extraports state="closed" count="995">
<extrareasons reason="conn-refused" count="995"/>
</extraports>
<port protocol="tcp" portid="22">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="ssh" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="25">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="smtp" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="111">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="rpcbind" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="631">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="ipp" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="3306">
<state state="open" reason="syn-ack" reason_ttl="1"/>
<service name="mysql" method="table" conf="3"/>
</port>
</ports>
<times srtt="2100" rttvar="688" to="100000"/>
</host>
"""

host3 = """<host starttime="13617" endtime="13617">
<status state="down" reason="localhost-response"/>
<address addr="127.0.0.1" addrtype="ipv4"/>
<hostnames>
<hostname name="localhost" type="user"/>
<hostname name="localhost" type="PTR"/>
</hostnames>
<ports><extraports state="closed" count="995">
<extrareasons reason="conn-refused" count="995"/>
</extraports>
<port protocol="tcp" portid="22">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="ssh" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="111">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="rpcbind" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="631">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="ipp" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="3306">
<state state="closed" reason="syn-ack" reason_ttl="0"/>
<service name="mysql" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="3307">
<state state="closed" reason="syn-ack" reason_ttl="0"/>
<service name="mysql" method="table" conf="3"/>
</port>
</ports>
<times srtt="2100" rttvar="688" to="100000"/>
</host>
"""
host4 = """
<host starttime="77" endtime="13">
<status state="up" reason="locaonse"/>
<address addr="127.0.0.1" addrtype="ipv4"/>
<hostnames>
<hostname name="localhost" type="user"/>
<hostname name="localhost" type="PTR"/>
</hostnames>
<ports><extraports state="azeazeaze" count="995">
<extrareasons reason="conn-refused" count="995"/>
</extraports>
<port protocol="tcp" portid="22">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="ssh" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="25">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="smtp" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="111">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="rpcbind" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="631">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="ipp" method="table" conf="3"/>
</port>
<port protocol="tcp" portid="3306">
<state state="open" reason="syn-ack" reason_ttl="0"/>
<service name="mysql" method="table" conf="3"/>
</port>
</ports>
<times srtt="200" rttvar="68" to="100"/>
</host>
"""


class TestNmapHost(unittest.TestCase):
    def test_eq_host(self):
        h1 = NmapParser.parse_host(host1)
        h2 = NmapParser.parse_host(host2)
        h3 = NmapParser.parse_host(host3)
        h4 = NmapParser.parse_host(host4)

        self.assertNotEqual(h1, h2)
        self.assertEqual(h1, h1)
        self.assertNotEqual(h1, h3)
        self.assertEqual(h1, h4)
        self.assertNotEqual(h2, h3)

    def test_diff_host(self):
        h1 = NmapParser.parse_host(host1)
        h2 = NmapParser.parse_host(host2)
        h3 = NmapParser.parse_host(host3)

        c1 = h1.diff(h2)
        c2 = h1.diff(h3)
        c3 = h2.diff(h3)

        self.assertEqual(c1.changed(), set(['hostnames']))
        self.assertEqual(c1.added(), set([]))
        self.assertEqual(c1.removed(), set([]))
        self.assertEqual(c1.unchanged(), set(['status',
                                              'NmapService.343309847',
                                              'NmapService.343309848',
                                              'NmapService.343309921',
                                              'NmapService.343309433',
                                              'address',
                                              'NmapService.343306980']))

        self.assertEqual(c2.changed(), set(['status',
                                            'NmapService.343306980']))
        self.assertEqual(c2.added(), set(['NmapService.343309847']))
        self.assertEqual(c2.removed(), set(['NmapService.343306981']))
        self.assertEqual(c2.unchanged(), set(['hostnames',
                                              'NmapService.343309848',
                                              'NmapService.343309921',
                                              'NmapService.343309433',
                                              'address']))

        self.assertEqual(c3.changed(), set(['status', 'hostnames',
                                            'NmapService.343306980']))
        self.assertEqual(c3.added(), set(['NmapService.343309847']))
        self.assertEqual(c3.removed(), set(['NmapService.343306981']))
        self.assertEqual(c3.unchanged(), set(['NmapService.343309848',
                                              'NmapService.343309921',
                                              'NmapService.343309433',
                                              'address']))


if __name__ == '__main__':
    test_suite = ['test_eq_host', 'test_diff_host']
    suite = unittest.TestSuite(map(TestNmapHost, test_suite))
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)