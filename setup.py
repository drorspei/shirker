from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='slacker',
    version='1.0.0',
    description='run command and send stdout+stderr to slack',
    long_description_content_type="text/markdown",
    license="MIT",
    long_description=long_description,
    author='Dror Speiser',
    url="http://github.com/drorspei/slacker",
    packages=['slacker'],
    install_requires=[
        "fsspec",
        "urllib3",
    ],
    entry_points={
        'console_scripts': [
            'slacker = slacker.main:main',
        ],
    },
)
