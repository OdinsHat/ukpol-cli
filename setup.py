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
    description='A CLI tool for finding information on local police force',
    long_description=read('README.md'),
    author='Doug Bromley',
    author_email='doug@tintophat.com',
    url='',
    reuires=REQUIRES,
    license=read('LICENSE'),
    keywords='uk police force crime stats data information',
    py_modules=["ukpol_cli"],
    entry_points={
        'console_scripts': [
            "ukpol = ukpol_cli:cli"
        ]
    },
)