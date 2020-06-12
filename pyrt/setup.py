from setuptools import setup, find_packages

requirements = [ 
    "pytest==5.4.2",
    "setuptools==46.4.0",
    "numpy==1.18.1",
    "Pillow==7.1.2",
    "tqdm==4.46.0",
    "redis==3.5.3", 
    "celery==4.4.0",
    "requests==2.23.0"
    ]

setup(
    name='pyrt',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=requirements
)
