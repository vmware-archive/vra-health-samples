# VMware vSphere Python SDK Community Samples
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import find_packages, setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='vrealize-health-samples',
      version='1.0.0.dev',
      description='VMware vRealzie Health Service Python SDK Samples',
      author='VMware, Inc.',
      author_email='jeffcook@vmware.com',
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