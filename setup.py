from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove[HYPEN_E_DOT]
        return requirements

setup(
    name='fault dection',
    version='0.0.1',
    author='divya',
    insatll_requirements=['requirements.txt'],
    packages=find_packages()
)