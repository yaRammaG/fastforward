import sys, os

try:
    from setuptools import setup, find_packages
except ImportError:
    print("fastforward now needs setuptools in order to build. Install it using"
          " your package manager (usually python-setuptools) or via pip (pip"
          " install setuptools).")
    sys.exit(1)

from fastforward import __version__, __author__

def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        f = open(path)
    except IOError:
        return None
    return f.read()

setup(name='fastforward',
    version=__version__,
    description='FastForward is a DevOps automate platform',
    long_description=read('README.md'),
    author=__author__,
    author_email='jiasir@icloud.com',
    url='https://github.com/nofdev/fastforward',
    license='MIT',
    install_requires=['playback == 0.3.4'],
    packages=find_packages(),
    entry_points={ 
       'console_scripts': [
           'ff = fastforward.cli:main',
           ],

        'openstack': [
            'environment = fastforward.environment:make'
        ],
       },
    )
