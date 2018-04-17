from setuptools import setup, find_packages

with open('README.rst','r') as f:
    readme = f.read()

setup(
    name='f5-client',
    version='0.0.13',
    description='Manage F5 using f5-sdk',
    long_description=readme,
    author='amintej',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[ 'f5-sdk','PrettyTable','IPy' ],
    entry_points={
        'console_scripts': [
           'f5-client=f5client.f5cli:main',
        ]
   }

)
