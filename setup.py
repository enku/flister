from setuptools import setup, find_packages

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name='flister',
    version='0.0',
    description='file browser written in Django',
    long_description=long_description,
    author='Albert Hopkins',
    author_email='marduk@letterboxes.org',
    packages=find_packages('.'),
    package_data = {
        'flister': ['flister/templates/listing.html'],
    },
    license='BSD',
    install_requires=[
        'django',
    ]
)
