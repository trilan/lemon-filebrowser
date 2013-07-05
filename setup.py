import codecs
import os
from setuptools import setup, find_packages


def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    return codecs.open(filepath, encoding='utf-8').read()


setup(
    name='lemon-filebrowser',
    version='0.1.2',
    license='ISC',
    description="Fork of Patrick Kranzlmueller's django-filebrowser app.",
    url='https://github.com/trilan/lemon-filebrowser',
    author='Trilan Team',
    author_email='dev@lemon.io',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
