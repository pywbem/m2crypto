========= M2Crypto =========

:Maintainer: Heikki Toivonen :Web-Site:
https://gitlab.com/m2crypto/m2crypto

M2Crypto = Python + OpenSSL + SWIG
----------------------------------

M2Crypto is a crypto and SSL toolkit for Python.

M2 stands for "me, too!"

M2Crypto comes with the following:

-  **RSA**, **DSA**, **DH**, **HMACs**, **message digests**, **symmetric
   ciphers** including **AES**,

-  **SSL/TLS** functionality to implement **clients and servers**.

-  **Example SSL/TLS client and server programs**, which are variously
   **threading**, **forking** or based on **non-blocking socket IO**.

-  **HTTPS** extensions to Python's **httplib, urllib and xmlrpclib**.

-  Unforgeable HMAC'ing **AuthCookies** for **web session management**.

-  **S/MIME v2**.

-  And much more.

-  Project with demo applications using M2Crypto is now in the separate
  project available at https://gitlab.com/m2crypto/m2crypto_demo

M2Crypto is released under a very liberal BSD-style licence. See LICENCE
for details.

To install, see the file INSTALL.

Look at the tests and demos for example use. Recommended reading before
deploying in production is "Network Security with OpenSSL" by John
Viega, Matt Messier and Pravir Chandra, ISBN 059600270X.

Note these caveats:

-  Possible memory leaks, because some objects need to be freed on the
   Python side and other objects on the C side, and these may change
   between OpenSSL versions. (Multiple free's lead to crashes very
   quickly, so these should be relatively rare.)

-  No memory locking/clearing for keys, passphrases, etc. because AFAIK
   Python does not provide the features needed. On the C (OpenSSL) side
   things are cleared when the Python objects are deleted.

Have fun! Your feedback is welcome.
