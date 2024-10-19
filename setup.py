from setuptools import setup,find_packages

hypen_dot_e= '-e .'

def get_requirements(name: str):
    requirements=[]
    with open('requirements.txt','r') as f:
        requirements=f.readlines()
        requirements=[ requirement.strip() for requirement in requirements]
        if hypen_dot_e in requirements:
            requirements=requirements.remove(hypen_dot_e)
    return requirements



setup(name='nlpproject',
      version='1.4.3',
      description='nplend to end project',
      author='simhadri sriram',
      author_email='simhadrisriram3@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
      )