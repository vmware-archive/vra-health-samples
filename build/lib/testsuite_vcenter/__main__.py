import sys
from testsuite_vcenter.vcenter import vCenterTestSuite

print("Executing Suite of Tests with " + str(sys.argv))
suite = vCenterTestSuite()
suite.run_tests(*sys.argv)
