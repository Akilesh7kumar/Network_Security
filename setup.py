'''

'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:

    requirement_list:List[str] = []
    try:
        with open ('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                req = line.strip()
                if req and req != '-e .':
                    requirement_list.append(req)
    except FileNotFoundError as e:
        print(e)
    return requirement_list

setup(
    name="Network_Security",
    version="0.0.1",
    author="Akilesh",
    author_email="akilesh.ramkumar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
