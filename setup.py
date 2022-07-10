import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requirements = []
with open('requirements.txt') as f:
    for line in f:
        install_requirements.append(line)

setuptools.setup(
    name="btextra",
    version="0.0.1",
    author="Abhilash Nanda",
    author_email="wishabhilash@gmail.com",
    description="Extra libs for backtrader.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wishabhilash/btextra",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Proprietary",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requirements,
    python_requires='>=3.9.5',
)