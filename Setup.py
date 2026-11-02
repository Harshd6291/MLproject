from weakref import ref

from setuptools import find_packages, setup
from typing import list 
def get_requirement(file_path:str)-> list[str]:
    '''
    this function will return the list of requirements'''
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]

setup(
    name="MLproject",
        version="0.0.1"
)
