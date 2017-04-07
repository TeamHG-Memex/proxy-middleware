proxy-middleware
================

.. image:: https://img.shields.io/pypi/v/proxy-middleware.svg
   :target: https://pypi.python.org/pypi/proxy-middleware
   :alt: PyPI Version

Scrapy middleware that reads proxy config from settings.

Install::

    pip install proxy-middleware

Usage: add it to ``DOWNLOADER_MIDDLEWARES`` in scrapy settings::

    DOWNLOADER_MIDDLEWARES = {
       'proxy_middleware.ProxyFromSettingsMiddleware': 10,
       ...

Pass proxy config via ``HTTP_PROXY`` and ``HTTPS_PROXY`` settings
variables. ``HTTPPROXY_AUTH_ENCODING`` is also respected::

    scrapy crawl my-spider -s HTTP_PROXY=http://localhost:8118

License is MIT.
