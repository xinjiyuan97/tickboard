from setuptools import setup, find_packages
setup(
    name = "tickboard",
    version = '0.1',
    author = "xinjiyuan97",
    author_email = "xinjiyuan97@163.com",
    packages = find_packages(),
    install_requires = [
        'flask'
    ],
    entry_points = {
        "console_scripts": [
            'tickboard = tickboard.__main__:cli'
        ]
    }
)