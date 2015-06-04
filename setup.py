#!/usr/bin/env python

from setuptools import setup

setup(name='docutils-htmlwriter',
      version='0.3',
      description='Another HTML Writer for Docutils',
      long_description=open('README.rst').read(),
      author='IGARASHI Masanao',
      author_email='syoux2@gmail.com',
      url='http://github.com/masayuko/docutils-htmlwriter',
      packages=['htmlwriter'],
      license='MIT',
      keywords='website, static',
      classifiers=(
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: Plugins',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: OS Independent',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Documentation',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing'),
      install_requires=['docutils'],
      include_package_data=True,
      entry_points = {
          'console_scripts': [
              'rst2htmlr = htmlwriter.rst2htmlr:main'
          ]
      },
)
