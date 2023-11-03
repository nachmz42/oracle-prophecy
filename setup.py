from setuptools import find_packages, setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='oracle-prophecy',
      version='0.1.0',
      description='Oracle Prophecy',
      license='MIT',
      install_requires = requirements,
      packages=find_packages(),
      test_suite='tests',
      include_package_data=True,
      zip_safe=True)
