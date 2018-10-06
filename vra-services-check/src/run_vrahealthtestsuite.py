#import json
print("CHECK: About to execute 'from testsuite_module.vrahealthtestsuite import vRAUpgradeTestSuite'..")
import  json
from testsuite_module.vrahealthtestsuite import vRAUpgradeTestSuite

if __name__ == '__main__':
    suite = vRAUpgradeTestSuite()

    print("Test vRA Post upgrade Health Tests dev CLI run: writing results back to the Python Test Service will likely fail, but doesn't affect test correctness")
    print ("-------------------------------------------------------------------------------------------------")

    # Used to write results to test service
    # Can ignore and just let that part fail.
    # initialize variables to empty strings
    host = ''
    configuration = ''
    overall_result = ''
    test_suite= ''
    token = ''
	
    # Change these to match the test suite arguments
    args = [
        {
            "name":  "vraaddress",
            "value": "https://cava-n-80-199.eng.vmware.com",
            "type":  "String"
        },
        {
            "name":  "vrausername",
            "value": "administrator@vsphere.local",
            "type":  "String"
        },
        {
            "name":  "vrapassword",
            "value":  "VMware1!",
            "type":  "Password"
        },
        {
            "name": "numservices",
            "value": 22,
            "type": "Integer"
        },
        {
            "name": "numendpoints",
            "value": 21,
            "type": "Integer"
        },

        {
            "name":  "vratenant",
            "value": "vsphere.local",
            "type":  "String"
        },
        {
            "name":  "vranondeftenant",
            "value": "qe",
            "type":  "String"
        },
        {
            "name":  "vratenantusername",
            "value": "tenantadmin@vsphere.local",
            "type":  "String"
        },
        {
            "name":  "vratenantpassword",
            "value": "P@ssword01",
            "type":  "Password"
        },
         {
            "name": "numrestypes",
            "value": 15,
            "type": "Integer"
        }


    ]
	
    #Now, run the test suite
    suite.run_tests(":-", host, configuration, overall_result, test_suite,token, json.dumps(args))
