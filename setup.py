import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='proxy-middleware',
    version='0.2.0',
    description=('Scrapy http proxy middleware that gets '
                 'proxy parameters from settings'),
    license='MIT',
    url='https://github.com/TeamHG-Memex/proxy-middleware',
    packages=['proxy_middleware'],
    install_requires=[
        'scrapy>=1.1.0',
    ],
    long_description=read('README.rst') + '\n\n' + read('CHANGES.rst'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
