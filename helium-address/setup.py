from setuptools import setup, find_packages

setup(
    name="helium-address",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "base58>=2.1.0",
    ],
    entry_points={
        'console_scripts': [
            'helium-convert=helium_address.cli:main',
        ],
    },
    author="Jose Marcelino",
    author_email="jm@maneki.net",
    description="Helium public key utilities",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jmarcelino/helium-utils/helium-address",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0",
        "Operating System :: OS Independent",
    ],
    keywords=["helium"],
    python_requires=">=3.6",
)
