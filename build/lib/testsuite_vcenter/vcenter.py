################################################################################################
#
# Test Implementation
#
################################################################################################
#from testsuitebase.testsuitebase import test_parameter, test_suite, TestSuiteBase, test, test_name, test_description, test_severity, test_access_level, test_remediation, AccessLevel, Severity
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

