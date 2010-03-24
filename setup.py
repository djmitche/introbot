from setuptools import Command, setup, find_packages

setup(name='introbot',
      version="1.0",
      description='A lalita-based bot framework so beginner programmers can write IRC bots',
      author='Dustin J. Mitchell',
      author_email='dustin@v.igoro.us',
      url='http://github.com/djmitche/introbot',
      packages=find_packages(),
      install_requires = [ 'lalita' ],
      entry_points = { 
        'console_scripts': [
          'introbot=introbot.main:introbot',
          'textbot=introbot.main:textbot',
        ],  
      },  
      )   
