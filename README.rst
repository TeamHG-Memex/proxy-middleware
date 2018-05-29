proxy-middleware
================

.. image:: https://img.shields.io/pypi/v/proxy-middleware.svg
   :target: https://pypi.python.org/pypi/proxy-middleware
   :alt: PyPI Version

Scrapy middlewares that reads proxy config from settings.

.. contents::

Install
-------

::

    pip install proxy-middleware


ProxyFromSettingsMiddleware
---------------------------

A middleware that sets proxy from settings file.

Usage: add it to ``DOWNLOADER_MIDDLEWARES`` in scrapy settings::

    DOWNLOADER_MIDDLEWARES = {
       'proxy_middleware.ProxyFromSettingsMiddleware': 10,
       ...

Pass proxy config via ``HTTP_PROXY`` and ``HTTPS_PROXY`` settings
variables. ``HTTPPROXY_AUTH_ENCODING`` is also respected::

    scrapy crawl my-spider -s HTTP_PROXY=http://localhost:8118


ProxyOnlyTorMiddleware
----------------------

A middleware that proxies only requests to TOR sites (domain ends with ".onion").

Usage: add it to ``DOWNLOADER_MIDDLEWARES`` in scrapy settings::

    DOWNLOADER_MIDDLEWARES = {
       'proxy_middleware.ProxyOnlyTorMiddleware': 10,
       ...

Settings: ``HTTP_PROXY`` for an http proxy and ``HTTPS_PROXY`` for an https proxy.


License
-------

License is MIT.

----

.. image:: https://hyperiongray.s3.amazonaws.com/define-hg.svg
	:target: https://www.hyperiongray.com/?pk_campaign=github&pk_kwd=proxy-middleware
	:alt: define hyperiongray
