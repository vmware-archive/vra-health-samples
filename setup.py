# VMware vSphere Python SDK Community Samples
#
# Copyright 2018 VMware, Inc.  All rights reserved				

# The MIT license (the “License”) set forth below applies to all parts of the VMware vRealize Health Service Code Samples project.  You may not use this file except in compliance with the License. 

# MIT License

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from setuptools import find_packages, setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='vrealize-health-samples',
      version='1.0.0.dev',
      description='VMware vRealize Health Service Python SDK Samples',
      author='Author',
      author_email='author@email.com',
      url='http://vmware.github.io/vrhb-community-samples/',
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