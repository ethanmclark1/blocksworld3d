"""Setups up the Blocksworld module."""

from setuptools import setup

setup(
    name="blocksworld",
    version="0.1.1",
    author="Ethan Clark",
    author_email="eclark715@gmail.com",
    description="Minimalistic 3D interior environment simulator for reinforcement learning & robotics research.",
    url="https://github.com/ethanmclark1/blocksworld",
    license="Apache",
    license_files=("LICENSE",),
    keywords=["Environment", "Agent", "RL", "Gym", "Robotics", "3D"],
    python_requires=">=3.7, <3.11",
    packages=["blocksworld", "blocksworld.envs"],
    package_data={"blocksworld": ["textures/*.png",]},
    extras_require={"testing": ["pytest==7.0.1", "torch"]},
    install_requires=[
        "numpy>=1.18.0",
        "pyglet==1.5.27",
        "gymnasium>=0.26.2",
    ],
    # Include textures and meshes in the package
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
