from setuptools import setup

name = 'leetcode-dl'
packages = [
    "leetcode_dl",
    "leetcode_dl_cli"
]


setup(
    name=name,
    version='0.1.0',
    keywords=('leetcode', 'download'),
    description='Command-line program to download solutions from leetcode.com',
    download_url='https://pypi.python.org/pypi/{}'.format(name),
    long_description='https://github.com/bonfy/{}'.format(name),
    license='MIT License',
    author='bonfy',
    author_email='foreverbonfy@163.com',
    install_requires=[
        'requests',
        'clint',
        'pyquery'
    ],
    packages=packages,
    platforms='any',
    entry_points={'console_scripts': 'leetcode-dl=leetcode_dl_cli.main:main'},
)