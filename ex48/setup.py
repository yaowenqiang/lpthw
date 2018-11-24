try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description"："ex48",
    "author": "yaowenqiang",
    "url": "URL to get it at.",
    "download_url":"Where to download it",
    "author_email":"yaowenqiang111@163.com",
    "version":"0.1",
    "install_requires":['nuse'],
    "packages":["ex48"],
    "scripts":[],
    "name":"ex48"
}
setup(**config)

