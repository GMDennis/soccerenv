
from setuptools import setup, find_packages
import sys, os.path

sys.path.insert(0, os.path.join(osh.path.dirname(__file__), 'soccerenv'))

setup(name='soccerenv',
      version='1.0',
      description='Soccerenv described in correlated-Q Learning',
      author='emoudahi',
      author_email='',
      license='',
      packages=setuptools.find_packages(),
      zip_safe=False,
      url='https://github.com/GMDennis/soccerenv.git',
      python_requires='>=3.6')
