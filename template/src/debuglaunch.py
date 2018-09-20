import json
from testsuite_your_package.testsuite import YourTestSuite

if __name__ == '__main__':
    suite = YourTestSuite()

    print("Test basic tests functionality, writing results back to the Python Test Service will likely fail, but doesn't affect test correctness")

    # Used to write results to health service
    # Can be ignored for local testing.
    host = ''
    configuration = ''
    overall_result = ''
    test_suite= ''
    token = ''


    ##################################################
    # Change these to match the test suite arguments
    args = [
        {
            "name":  "your_package_address",
            "value": "server.local",
            "type":  "String"
        },
        {
            "name":  "your_package_username",
            "value": "root",
            "type":  "String"
        },
        {
            "name":  "your_package_port",
            "value":  "443",
            "type":  "String"
        },
        {
            "name":  "your_package_password",
            "value": "VMware1!",
            "type":  "Password"
        }
    ]

    suite.run_tests("-", host, configuration, overall_result, test_suite,token, json.dumps(args))

