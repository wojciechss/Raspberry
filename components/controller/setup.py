r"""
Raspberry controller
"""

from setuptools import setup, find_packages

setup(
    name='controller',
    version='0.0.1',
    author='Wojciech Jozwiak',
    description='Raspberry controller',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=['requests', 'gunicorn', 'falcon', 'pyserial']
)
