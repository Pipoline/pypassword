import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypassword",
    version="0.0.3",
    author="Peter Gonda",
    author_email="peter@pipoline.com",
    description="Simple password generator module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pipoline/random-password",
    packages=setuptools.find_packages(),
    license="MIT",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
