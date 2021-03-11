#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=7.0',
                "numpy==1.18.1",
                "Pillow==7.1.2",
                "tqdm==4.46.0",
                "redis==3.5.3",
                "celery==4.4.0",
                "requests==2.23.0"]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Steffen Deubler",
    author_email='steffen.deubler@t-online.de',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="An python-based raytracer inspired by the book Raytracing in one Weekend",
    entry_points={
        'console_scripts': [
            'pyrt=pyrt.__main__:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='pyrt',
    name='pyrt',
    packages=find_packages(include=['pyrt', 'pyrt.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sdeu/pyrt',
    version='0.1.0',
    zip_safe=False,
)
