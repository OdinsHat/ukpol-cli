from setuptools import setup


REQUIRES = [
    'requests>=2.3.0',
    'click>=2.0',
]


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='ukpol-cli',
    version='0.0.1',
    description='A CLI tool for finding information on UK police forces and local crime information',
    long_description=read('README.md'),
    author='Doug Bromley',
    author_email='doug@tintophat.com',
    url='https://github.com/OdinsHat/ukpol-cli',
    download_url='https://github.com/OdinsHat/ukpol-cli/archive/master.zip',
    reuires=REQUIRES,
    license=read('LICENSE'),
    keywords='uk police force crime stats data information cli',
    py_modules=["ukpol_cli"],
    entry_points={
        'console_scripts': [
            "ukpol = ukpol_cli:cli"
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Beta'
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)