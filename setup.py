import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.txt")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()

requires = [
    "pyramid",
    "pyramid_beaker",
    "pyramid_debugtoolbar",
    "Akhet",
    "waitress",
    ]

entry_points = """\
[paste.app_factory]
main = akhet_demo:main
"""

setup(name="akhet_demo",
      version="1.0",
      description="A Pyramid demo app inspired by Pylons.",
      long_description=README + "\n\n" +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Programming Language :: Python",
        "License :: OSI Approved : MIT License",
        ],
      author="Mike Orr",
      author_email="sluggoster@gmail.com",
      url="https://github.com/mikeorr/akhet_demo",
      license="MIT",
      keywords="web pyramid pylons",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="akhet_demo",
      entry_points = entry_points,
      )

