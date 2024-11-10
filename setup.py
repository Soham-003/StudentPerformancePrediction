from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path : str)-> List[str]:
    # function will returning list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #reads the entire file into a list, but it includes newline characters (\n) at the end of each line.
        requirements=[req.replace("\n","") for req in requirements] #removing those extra newline characters, ensuring that each requirement is a clean string.

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    #metadata
    name = 'MLproject',
    version = '0.0.1',
    author = "Soham",
    author_email = "sohamsawankhanna@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')
)