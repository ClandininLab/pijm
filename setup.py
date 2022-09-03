from setuptools import setup

setup(
    name="PIJM",
    version="0.1.1",
    author="Andrew Berger",
    author_email="a5b@stanford.edu",
    description="PIJM is just matplotlib. Tools for visualization of dense 3D imagery.",
    url="https://github.com/ClandininLab/pijm",
    packages=["pijm"],
    python_requires=">=3.6",
    install_requires=["matplotlib", "numpy"],
)
