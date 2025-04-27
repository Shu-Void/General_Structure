from setuptools import find_packages,setup
# This automatically finds packages used in ml project
from typing import List

hyphen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    # Function to read required packages from requirements.txt
    with open(file_path) as f_object:
        requirements = f_object.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    
    return requirements


setup(
    name='ML project',
    version='0.0.1',
    author='Shu_Void',
    author_email='sudhanshuprabhatofficial@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)