from setuptools import setup, find_packages

setup(
    name='school_service_grpc',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        "grpcio",
        "grpcio-tools"
    ],
)