""" 
vRealiza Automation Test Suite Setup 

Setuptools configuration for building the wheel for the Infoblox test extension.

Copyright © 2018 VMware, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the “License”); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at http://www.apache.org/licenses/LICENSE-2.0
  
Some files may be comprised of various open source software components, each of which
has its own license that is located in the source code of the respective component.
"""

from setuptools import find_packages, setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='vrealize-health-vra-dev',
      version='1.0.0',
      description='VMware vRealize Automation Post Upgrade Health Service Checks ',
      author='VMware, Inc.',
      author_email='dzilberman@vmware.com',
      url='https://github.com/vmwaresamples/vra-health-samples',
      install_requires=['pyvmomi'],
      packages=find_packages(where="src"),
      package_dir={"": "src"},
      license='Apache',
      long_description=read('README.md'),
      python_requires='>=3',
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Development Status :: 4 - Beta",
          "Environment :: No Input/Output (Daemon)",
          "Intended Audience :: Information Technology",
          "Intended Audience :: System Administrators",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System :: Distributed Computing"
      ],
      zip_safe=True)
