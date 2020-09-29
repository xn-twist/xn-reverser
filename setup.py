#!/usr/bin/env python3
from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

install_requirements = [
    "idna",
]

setup(name='xn-reverser',
      version='1.0.0',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description='Enumerate possible ASCII text being spoofed by a particular IDN domain name',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/xn-twist/xn-reverser',
      author='wesinator',
      author_email='13hurdw@gmail.com',
      include_package_data=True,
      install_requires=install_requirements,
      packages=['xn_reverser'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
      ],
      zip_safe=False)
