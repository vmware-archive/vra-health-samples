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

import atexit
import ssl

from pyVim import connect
from pyVmomi import vmodl

@test_parameter('vcenter', 'vCenter Appliance', 'vcaddress', 'vCenter Appliance Address', 'server', 'String', '')
@test_parameter('vcenter', 'vCenter Appliance', 'vcusername', 'vCenter Appliance Username', 'root', 'String', 'root')
@test_parameter('vcenter', 'vCenter Appliance', 'vcpassword', 'vCenter Appliance Password', 'password', 'Password', '')
@test_parameter('vcenter', 'vCenter Appliance', 'vcport',   'vCenter Appliance Port',   '443', 'String', '443')
@test_suite('vCenter Tests', 'A collection of vCenter of tests', 'VMware vCenter', 6, 5, 0)
class vCenterTestSuite(TestSuiteBase):

    @test_name("Check Username")
    @test_description("Checks the value of username.")
    @test_access_level(AccessLevel.NORMAL.value)
    @test_severity(Severity.NORMAL.value)
    @test_remediation("http://www.google.com")
    @test
    def check_username(self,
                       vcusername
                       ):
        assert vcusername == 'administrator@vsphere.local', "expected 'root' but got " + vcusername
        return True

    @test_name("Check vCenter Connectivity")
    @test_description("Checks that the vcenter can be accessed.")
    @test_access_level(AccessLevel.NORMAL.value)
    @test_severity(Severity.NORMAL.value)
    @test_remediation("http://www.google.com")
    @test
    def check_vc_connectivity(self,
                              vcaddress,
                              vcusername,
                              vcpassword,
                              vcport
                         ):
        try:
            context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            context.verify_mode = ssl.CERT_NONE
            service_instance = connect.SmartConnect(host=vcaddress,
                                                    user=vcusername,
                                                    pwd=vcpassword,
                                                    port=int(vcport),
                                                    sslContext=context)

            atexit.register(connect.Disconnect, service_instance)

            session_id = service_instance.content.sessionManager.currentSession.key
            assert session_id != None, "Failed to connect to vCenter"

        except vmodl.MethodFault as error:
            assert False, "Caught exception: " + error.msg

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
    suite = vCenterTestSuite()
    suite.register_tests_with_framework(host, token, modulename, venv)

