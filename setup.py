
from setuptools import setup, find_packages
import sys, os.path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'soccerenv'))

setup(name='soccerenv',
      version='1.0',
      description='Soccerenv described in correlated-Q Learning',
      author='emoudahi',
      author_email='',
      license='',
      packages=[package for package in find_packages()
                if package.startswith('soccerenv')],
      zip_safe=False,
      install_requires=[
          'gym>=0.14.0'
      ],
      url='https://github.com/GMDennis/soccerenv.git',
      python_requires='>=3.6')
