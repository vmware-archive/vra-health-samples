# VMware vRA Health test Python SDK Community Samples
#
# Copyright 2018 VMware, Inc.  All rights reserved				

# The MIT license (the “License”) set forth below applies to all parts of the VMware vRealize Health Service Code Samples project.  You may not use this file except in compliance with the License. 

# MIT License

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#print("CHECK: About to execute 'from testsuite_module.vrahealthtestsuite import vRAUpgradeTestSuite'..")
import  json
from testsuite_module.vrahealthtestsuite import vRAUpgradeTestSuite

if __name__ == '__main__':
    suite = vRAUpgradeTestSuite()

    print("vRA Post upgrade Health Tests dev CLI run: writing results back to the Python Test Service will likely fail, but doesn't affect test correctness")
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
