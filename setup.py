import setuptools

setuptools.setup(
    name="pychronic",
    version="0.0.8",
    author="jayeshathila",
    author_email="sharma.jayesh52@gmail.com",
    description="A library to convert datetime to natural human readable format",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    extras_require={"test": ["pytest", "pytest-runner", "pytest-cov", "pytest-pep8"]},
)
