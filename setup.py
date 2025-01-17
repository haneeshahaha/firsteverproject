from setuptools import find_packages, setup
from typing import List

HYPE='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
         requirements=file_obj.readlines()
         requirements=[req.replace("\n","") for req in requirements]
         if HYPE in requirements:
              requirements.remove(HYPE)
    return requirements          

        
    setup(
    name='my_first_project_',
    version='0.0.1',
    author='haneesh',
    author_email='hburada@gitam.in',
    packges=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)