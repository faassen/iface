import os
from setuptools import setup, find_packages

def read(*filenames):
    return open(os.path.join(os.path.dirname(__file__), *filenames)).read()

# long_description = (
#     read('src', 'traject', 'traject.txt')
#     + '\n' +
#     read('CHANGES.txt')
#     + '\n' +
#     'Download\n'
#     '********\n'
#     )

setup(name='iface',
      version = '0.11dev',
      description="Interfaces and lookup for Python.",
      long_description='',
      # Use classifiers that are already listed at:
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Zope Public License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries',
                   ],
      keywords="interface interfaces",
      author="Martijn Faassen and Thomas Lotze",
      author_email="faassen@startifact.com",
      license="ZPL",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zope.interface',
                        'zope.component',
                        ],
      entry_points="""
      # Add entry points here
      """,
      )
