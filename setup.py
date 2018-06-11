from setuptools import setup, find_packages

with open('README.md') as readme_file:
    long_description = readme_file.read()

with open('VERSION') as version_file:
    version = version_file.read()

setup(
    name='youtube-data',
    version=version,
    description='A library to interact with Youtube.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Raül Pérez',
    author_email='hellol@vtalks.net',
    url='https://github.com/vtalks/youtube_data',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    license='Apache 2',
    test_suite='tests',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
