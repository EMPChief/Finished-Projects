from setuptools import setup

setup(
    name='indicator',
    version='0.1',
    description='A library of technical indicators for Python.',
    author='Google',
    author_email='noreply@google.com',
    license='Apache License 2.0',
    packages=['indicator'],
    install_requires=['pandas', 'numpy']
)
