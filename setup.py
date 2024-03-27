from setuptools import setup, find_packages

setup(
    name='simple encryption',
    version=0.1,
    packages=find_packages(),
    install_requires=[
       "<numpy> >= <1.17.4>;platform_system=='<Linux>'"
    ],
    author='Khanh Nguyen'
)