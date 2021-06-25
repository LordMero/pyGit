import setuptools, find_packages
from __init__ import __version__, __author__

setup(
        name="pygit",
        version=__version__,
        description="A small utility to handle github repos right from your terminal.",
        author=__author__,
        packages=find_packages(include=["pygit", "pygit.*"]),
        install_requires=["rich"],
        entry_points={
            "console_scripts": ["pygit=pygit.pygit:main"]
            }
        )
