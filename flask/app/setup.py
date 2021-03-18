from setuptools import find_packages, setup

setup(
    name='mock',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask==1.1.2',
        'dpath==2.0.1',
        'requests==2.24.0',
    ],
    python_requires='>3.7',
    description='An Flask service that loads raw text data from source, through ML services and returns the result.'
)