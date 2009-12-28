
from setuptools import setup

setup(name='lazycopy',
      version='0.0.1',
      author='Solomon Hykes <solomon.hykes@dotcloud.com>',
      install_requires=['distribute', 'aufs'],
      package_dir = {'lazycopy' : '.'},
      packages=['lazycopy'],
      scripts=['bin/lazycopy'],
      dependency_links = ['http://dotcloud.org.s3.amazonaws.com/aufs-0.0.1.tar.gz']
)
