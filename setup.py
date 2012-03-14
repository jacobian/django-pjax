import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'django-pjax',
    version = '1.2',
    description = 'A Django helper for jQuery-PJAX.',
    license = 'BSD',
    long_description = read('README.rst'),
    url = 'https://github.com/jacobian/django-pjax',

    author = 'Jacob Kaplan-Moss',
    author_email = 'jacob@jacobian.org',

    py_modules =  ['djpjax'],
    install_requires = ['django>=1.3'],

    classifiers = (
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
    ),
)
