from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    with open('requirements.txt', 'r') as file:
        packages = [line.strip() for line in file if line.strip()]

    if HYPEN_E_DOT in packages:
            packages.remove(HYPEN_E_DOT)

    return packages


setup(
name='mlproject',
version='0.0.1',
author='Satwik',
author_email='satwiksharma470@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)