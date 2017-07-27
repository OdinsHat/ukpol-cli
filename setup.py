from setuptools import setup


REQUIRES = [
    'requests>=2.3.0',
    'click<3.0',
]


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='ukpol-cli',
    version='0.0.4',
    description='A CLI tool for finding information on UK police forces and local crime information',
    long_description=read('README.rst'),
    author='Doug Bromley',
    author_email='doug@tintophat.com',
    url='https://github.com/OdinsHat/ukpol-cli',
    download_url='https://github.com/OdinsHat/ukpol-cli/archive/master.zip',
    install_requires=REQUIRES,
    license='MIT',
    py_modules=["ukpol_cli"],
    entry_points={
        'console_scripts': [
            "ukpol = ukpol_cli:cli"
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Legal Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Console',
        'Topic :: Utilities',
        'Topic :: Terminals',
    ],
    keywords='uk, police, force, crime, stats, data, information, cli',
)
