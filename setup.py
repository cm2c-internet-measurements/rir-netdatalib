# setup.py
# lacniclabs datasets python library
# 20170310 v1
# 20170328 v 0.1.2
# 20170329 v 0.1.3


from setuptools import setup

setup(name='lacniclabs',
      version='0.1.4',
      description='cm2c python commons',
      url='https://github.com/LACNIC/labs-opendata-datasets',
      author='Carlos M. Martinez',
      author_email='carlos@lacnic.net',
      license='BSD',
      packages=['lacniclabs', 'lacniclabs.models', 'lacniclabs.utils',
		'lacniclabs.netdata', 'lacniclabs.etc'],
      install_requires=['ipaddr'],
      zip_safe=False)
