## Overview

This contains a Python Wheel Project that can be executed from the vRealize Health Service
Try it out
Prerequisites

    vRealize Automation 7.4 or above
    Python 3.5.x (or above) for local development
    vRealize Health Service SDK ('vmware_healthsvc_sdk-0.3.5-py3-none-any.whl' downloadable from vRealize Health Service Extensibility page)

## Test
    
    modify parameters in the ./src/run_vrahealthtestsuite.py to match the test target vRA environment and related test suite input parameters
    <path to python 3.5.x>/python ./src/run_vrahealthtestsuite.py
	
## Build & Run

    <path to python 3.5.x>/python setup_dev.py bdist_wheel
    upload ./dist/vrealize_health_vra_dev-1.0.0-py3-none-any.whl to the vRealize Health Service

## Contributing

The vra-healthtest-vra-sdk-samples project team welcomes contributions from the community. Before you start working with vra-healthtest-vra-sdk-samples, please read our Developer Certificate of Origin. All contributions to this repository must be signed as described on that page. Your signature certifies that you wrote the patch or have the right to pass it on as an open-source patch. For more detailed information, refer to CONTRIBUTING.md.
License

The MIT license (the “License”) set forth below applies to all parts of the VMware vRealize Health Service Code Samples project. You may not use this file except in compliance with the License. 

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
