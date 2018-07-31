from package_settings import NAME, VERSION, PACKAGES, DESCRIPTION
from setuptools import setup

setup(
    name=NAME,
    version=VERSION,
    long_description=DESCRIPTION,
    author='Bloomsbury AI',
    author_email='contact@bloomsbury.ai',
    packages=PACKAGES,
    include_package_data=True,
    install_requires=[
        'argon2-cffi==16.3.0',
        'peewee==3.5.2',
        'pytest==3.6.4',
    ],
    package_data={
        '': ['*.*'],
    },
)
