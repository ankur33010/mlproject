from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT="-e ."


def get_requirements(filepath: str)-> List[str]:

    """
    This Function will return the list of requiremnts
    
    """
    requirements=[]
    with open(filepath) as file:
        requirements=file.readlines()
        requirements=[i.replace("\n","") for i in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
name='mlproject',
version='0.0.1',
author='Ankur',
author_email='ankurtyagi33010@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)