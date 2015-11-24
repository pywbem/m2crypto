"""Unit tests for M2Crypto.SSL offline parts

Copyright (C) 2006 Open Source Applications Foundation. All Rights Reserved.

Copyright (C) 2009-2010 Heikki Toivonen. All Rights Reserved.
"""

import doctest
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from M2Crypto import Rand, SSL, X509
from test_ssl import srv_host


class CheckerTestCase(unittest.TestCase):
    def test_checker(self):

        check = SSL.Checker.Checker(
            host=srv_host,
            peerCertHash='A889D8A9861AB18265E0D504F60F81BBDC288128')
        x509 = X509.load_cert('tests/server.pem')
        self.assertTrue(check(x509, srv_host))
        with self.assertRaises(SSL.Checker.WrongHost):
            check(x509, 'example.com')

        doctest.testmod(SSL.Checker)


class ContextTestCase(unittest.TestCase):
    def test_ctx_load_verify_locations(self):
        ctx = SSL.Context()
        with self.assertRaises(ValueError):
            ctx.load_verify_locations(None, None)

    def test_map(self):
        from M2Crypto.SSL.Context import map, _ctxmap
        self.assertIsInstance(map(), _ctxmap)
        ctx = SSL.Context()
        assert map()
        ctx.close()
        self.assertIs(map(), _ctxmap.singleton)

    def test_certstore(self):
        ctx = SSL.Context()
        ctx.set_verify(SSL.verify_peer | SSL.verify_fail_if_no_peer_cert, 9)
        ctx.load_verify_locations('tests/ca.pem')
        ctx.load_cert('tests/x509.pem')

        store = ctx.get_cert_store()
        self.assertIsInstance(store, X509.X509_Store)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CheckerTestCase))
    suite.addTest(unittest.makeSuite(ContextTestCase))
    return suite


if __name__ == '__main__':
    Rand.load_file('randpool.dat', -1)
    unittest.TextTestRunner().run(suite())
    Rand.save_file('randpool.dat')
