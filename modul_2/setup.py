from setuptools import setup, find_namespace_packages

setup(name='assistant_bot',
      python_requires='>3.4.0',
      version='0.1.0',
      description='Python core TEAM5 project',
      url='https://github.com/PIRomanCod/',
      author='TEAM5',
      author_email='Roman Pimonov <111997187+PIRomanCod@users.noreply.github.com>',
      license='MIT',
      install_requires=['prompt_toolkit'],
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['pa = assistant_bot.main:main']})