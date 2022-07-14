from setuptools import setup, find_packages


setup(
    name='showip',
    version='1.0.0',
    license='MIT',
    author="Viktor Varvaruk",
    author_email='viktorvarvaruk01@gmail.com',
    packages=find_packages(),
    url='https://github.com/varvaruk-v/showip',
    keywords='ip adress internet api',
    install_requires=[
          'requests',
      ],

)