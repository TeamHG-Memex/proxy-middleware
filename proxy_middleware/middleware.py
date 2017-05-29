# -*- coding: utf-8 -*-
from six.moves.urllib.parse import urlsplit

from scrapy.exceptions import NotConfigured
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware


__all__ = ['ProxyFromSettingsMiddleware', 'ProxyOnlyTorMiddleware']


class ProxyFromSettingsMiddleware(HttpProxyMiddleware):
    """
    A middleware that sets proxy from settings file.
    Settings: HTTP_PROXY for an http proxy and HTTPS_PROXY for an https proxy.
    """

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings):
        self.proxies = {}
        self.auth_encoding = settings.get('HTTPPROXY_AUTH_ENCODING')
        proxies = [
            ('http', settings.get('HTTP_PROXY')),
            ('https', settings.get('HTTPS_PROXY')),
        ]
        for type_, url in proxies:
            if url:
                self.proxies[type_] = self._get_proxy(url, type_)
        if not self.proxies:
            raise NotConfigured


class ProxyOnlyTorMiddleware(ProxyFromSettingsMiddleware):
    """
    A middleware that proxies only requests to TOR sites (domain ends with .onion).
    Settings: HTTP_PROXY for an http proxy and HTTPS_PROXY for an https proxy.
    """
    def process_request(self, request, spider):
        parsed = urlsplit(request.url)
        if not parsed.netloc.endswith('.onion'):
            return None
        return super(ProxyOnlyTorMiddleware, self).process_request(request, spider)
