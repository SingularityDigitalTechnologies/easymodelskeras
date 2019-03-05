import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='singularitytechnologies.easymodelskeras',
    version='0.1.0dev',
    author='Sam Lacey',
    author_email='sam.lacey@singularity-technologies.io',
    description='Easy to use Keras Machine Learning Model ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/singularitytechnologies/easymodelskeras',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)
