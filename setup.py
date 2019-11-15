from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["numpy", "pandas", "scipy"]

setup(
    name="croston",
    version="0.1.2.1",
    author="hm6",
    author_email="hmohammadi6545@gmail.com",
    description="croston model for intermittent time series",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/newelldatascience/croston",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)