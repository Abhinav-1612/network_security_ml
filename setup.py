'''
this setup.py file is an esssential part of packaging 
and distrubuting python projects .it is used by setuptolls 
(distutils in older python versions ) to duistributr thr 
configurations of project ,such as its meta 
data ,dependcies and more
'''

from setuptools import find_packages,setup # this will search in all folders and where initpy file present import it as package 
from typing import List

def get_requirements()->list[str]:
    '''
    this function will return list of requiremnts 
    '''
    requirement_lst:list[str]=[]# list of string creating
    # we include all in try block for exception handeling 
    try:
        with open('requirements.txt','r') as file:
            #read the lines from file
            lines =file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()#ignoring empty lines 
                #ignore the empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)# adding in this list wahtever there in txt 

    except FileNotFoundError:
        print("requirements .txt file not found")

    return requirement_lst    

# setting up metadata
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ahinav Singh",
    author_email="abhinavishu0311@gmail.com",
    packages=find_packages(),#find all the packages
    install_requires=get_requirements()#install all the libraries
)