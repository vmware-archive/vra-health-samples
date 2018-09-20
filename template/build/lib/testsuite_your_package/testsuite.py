# VMware vSphere Python SDK Community Samples
#
# Copyright 2018 VMware, Inc.  All rights reserved				

# The MIT license (the “License”) set forth below applies to all parts of the VMware vRealize Health Service Code Samples project.  You may not use this file except in compliance with the License. 

# MIT License

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


################################################################################################
#
# Test Implementation
#
################################################################################################
from testsuitebase.testsuitebase import *


@test_parameter('your-package', 'Your Package', 'your_package_address', 'Your Package Address', 'server', 'String', '')
@test_parameter('your-package', 'Your Package', 'your_package_username', 'Your Package Username', 'root', 'String', 'root')
@test_parameter('your-package', 'Your Package', 'your_package_password', 'Your Package Password', 'password', 'Password', '')
@test_parameter('your-package', 'Your Package', 'your_package_port',   'Your Package Port',   '443', 'String', '443')
@test_suite('Your Package Tests', 'A collection of Your Package of tests', 'Your Product', 6, 5, 0)
class YourTestSuite(TestSuiteBase):

    @test_name("Check Username")
    @test_description("Checks the value of username.")
    @test_access_level(AccessLevel.NORMAL.value)
    @test_severity(Severity.NORMAL.value)
    @test_remediation("http://www.google.com")
    @test
    def check_username(self,
                    your_package_username
                       ):
        assert your_package_username == 'root', "expected 'root' but got " + your_package_username
        return True

    


################################################################################################
#
# Test Execution
#
################################################################################################
def register(host, token, modulename, venv):
    """
    This method is called by the vRealize Health Service framework to register the test classes
    :param host: the host to register with
    :param token: the security token used to make the call
    :param modulename: the name of this module
    :param venv: name of the virtual environment that these tests will run it
    :return:
    """
    suite = YourTestSuite()
    suite.register_tests_with_framework(host, token, modulename, venv)

