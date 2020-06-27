from setuptools import setup
from flask_wow import __version__


with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()


setup( 
    name="flask-wow",
    version=__version__,
    description="A simple CLI Generator for flask apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='extension flask flask-extension flask-build-tool flask_now flask-now app-generator flask-app-generator app generator',
    url="https://github.com/ganquan881205/flask-wow.git",
    author="Cove",
    author_email="cove@happyeyez.com",
    license="BSD-3-Clause",
    license_files = "LICENSE.rst",

    packages=["flask_wow"],
    include_package_data=True,
    platforms="any",
    install_requires=[
        'flask>=1.0.2',
        'click>=7.0'
    ],
    scripts=[],
    entry_points={
        'console_scripts': [
            'flask-wow = flask_wow.cli:main'
        ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Framework :: Flask',
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    zip_safe=False,
    python_requires='>=3.6',
)
