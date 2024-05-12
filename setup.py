from setuptools import setup, find_packages

# Read the requirements.txt file
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
    
with open('readme.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='WaveFormer',  
    version='0.1.0', 
    description='A single unified Advanced Audio Processing toolkit, that provides both High-Level and Low-Level approaches to its extensive collection of tools.',
    long_description=long_description,
    author='Bloom Research',
    author_email='rosebloomresearch@gmail.com',
    packages=find_packages(),  
    package_data={'': ['rubberband_builds/*.dll']},
    install_requires=requirements,
    license='CC BY 4.0',
    long_description_content_type='text/markdown'
)
