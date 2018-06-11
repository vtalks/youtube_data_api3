from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('VERSION') as version_file:
    version = version_file.read()

setup(
    name='youtube_data',
    version=version,
    description='A library to interact with Youtube.',
    long_description=readme,
    author='Raül Pérez',
    author_email='hellol@vtalks.net',
    url='https://github.com/vtalks/youtube_data',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    license='Apache 2',
    test_suite='tests'
)