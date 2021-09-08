import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyblend",
    version="0.0.0",
    author="Ben Bartlett",
    author_email="benbartlett@stanford.edu",
    description="Python blender library",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bencbartlett/pyblend",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "fake-bpy-module-2.93"
    ],
)
