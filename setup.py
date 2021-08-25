import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='singularitytechnologies.easymodelskeras',
    version='0.1.13dev',
    author='Sam Lacey',
    author_email='sam.lacey@singularity-technologies.io',
    description='Easy to use Keras Machine Learning Model ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/singularitytechnologies/easymodelskeras',
    packages=setuptools.find_packages(),
    install_requires=[
        'absl-py==0.7.0',
        'astor==0.7.1',
        'backcall==0.1.0',
        'decorator==4.3.2',
        'gast==0.2.2',
        'grpcio==1.19.0',
        'h5py==2.9.0',
        'jedi==0.13.3',
        'Keras==2.2.4',
        'Keras-Applications==1.0.7',
        'Keras-Preprocessing==1.0.9',
        'Markdown==3.0.1',
        'numpy==1.16.2',
        'parso==0.3.4',
        'pexpect==4.6.0',
        'pickleshare==0.7.5',
        'prompt-toolkit==2.0.9',
        'protobuf==3.7.0',
        'ptyprocess==0.6.0',
        'Pygments==2.3.1',
        'PyYAML==4.2b1',
        'scipy==1.2.1',
        'singularitytechnologies.easymodels==0.1.10dev',
        'six==1.12.0',
        'tensorboard==1.12.2',
        'tensorflow==2.5.1',
        'termcolor==1.1.0',
        'traitlets==4.3.2',
        'wcwidth==0.1.7',
        'Werkzeug==0.14.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)
