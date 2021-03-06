import setuptools

long_description = "For full description, please go to [Documentation](https://aid.autoai.org)"

setuptools.setup(
    name="vectordb",
    version="1.0.0.1",
    author="Xiaozhe Yao",
    author_email="askxzyao@gmail.com",
    description="Key Value Database for Vectors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://vectordb.autoai.org",
    packages=['vectordb'],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Software Development",
    ],
    install_requires=[
        "pydantic",
        "torch",
        "plyvel"
        "numpy==1.21.2"
    ],
    project_urls={
        "Bug Tracker": "https://github.com/composedb/faissdb/issues",
        "Documentation": "https://aid.autoai.org",
        "Source Code": "https://github.com/autoai-org/aid",
    },
)