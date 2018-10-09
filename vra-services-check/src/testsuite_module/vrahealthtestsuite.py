# VMware vRealize Automation Python SDK Community Samples
#
# Copyright 2018 VMware, Inc.  All rights reserved				

# The MIT license (the “License”) set forth below applies to all parts of the VMware vRealize Health Service Code Samples project.  You may not use this file except in compliance with the License. 

# MIT License

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE..

################################################################################################
#
# Test Suite Implementation based on vRHB Service Extensibility SDK Guide
#
################################################################################################

from testsuitebase.testsuitebase import *

import requests
import ssl
import json
#instruction to suppress invalid cert warnings output
requests.packages.urllib3.disable_warnings()

@test_parameter('vra', 'vRealize Automation', 'vraaddress', 'vRA Appliance Address', 'https://server', 'String', '')
@test_parameter('vra', 'vRealize Automation', 'vrausername', 'vRA System  Tenant Username', 'username@domain.com', 'String', 'administrator@vsphere.local')
@test_parameter('vra', 'vRealize Automation', 'vrapassword', 'vRA System Tenant Password', 'password', 'Password', '')
@test_parameter('vra', 'vRealize Automation', 'vratenant',   'vRA System Tenant Name',   'vsphere.local', 'String', '')
@test_parameter('vra', 'vRealize Automation', 'vratenantusername', 'vRA Non Default  Tenant Username', 'username@domain.com', 'String', 'tenantadmin@vsphere.local')
@test_parameter('vra', 'vRealize Automation', 'vratenantpassword', 'vRA Non Default Tenant Password', 'password', 'Password', '')
@test_parameter('vra', 'vRealize Automation', 'vranondeftenant', 'vRA Non Default Tenant Name', 'qe', 'String', '')
@test_parameter('vra', 'vRealize Automation', 'numservices', 'Expected # of vRA services', 20, 'Integer', 20)
@test_parameter('vra', 'vRealize Automation', 'numendpoints', 'Expected # of distinct vRA endpoints', 20, 'Integer', 20)
@test_parameter('vra', 'vRealize Automation', 'numrestypes', 'Expected # of distinct Reservation types in Tenant', 10, 'Integer', 10)
@test_suite('vRA Post Upgrade Health Tests Samples', 'A Collection of vRA Post Upgrade Validation Tests', 'vRealize Automation', 7, 5, 0)
class vRAUpgradeTestSuite(TestSuiteBase):
    
    #start login to vRA tenant function definitiion
    def login_vra_token(self, url, user, pwd, tenant):

        payload1 = "{\"username\":\""+str(user)+"\",\"password\":\""+str(pwd)+"\",\"tenant\":\""+str(tenant)+"\"}"
        headers = {'Accept': "application/json",'Content-Type': "application/json",'Cache-Control': "no-cache"}

        try:
             response = requests.request("POST", url, data=payload1, headers=headers, verify=False)
             responseJSON = response.json()
             if responseJSON != None:
                 if  responseJSON.get('id'):
                     token = responseJSON['id']
                     #print("DEBUG: extracted vRA login token:!")
                 else:
                     #print ("DEBUG: failed to authenticate to vRA system tenant, API URL: "+url+ " as user: "+user+"\n")
                     token = None 
             else:
                 #print ("DEBUG: no HTTP response received from vRA system tenant, API URL: "+url)
                 token = None

        except Exception as exc:
             #print("Error: vRA login to: "+url+" failed with error message:" + str(exc))
             raise Exception("Failed to login to vRA system tenant  URL: "+url+ ", tenant: "+tenant+" as user: "+user+"\n")
        return token

    #end of login to vRA tenant function definition 


    #start function definition of 'get_registered_services'
    def get_registered_services(self,url,user,pwd,tenant):
   
        querystring = {"page":"1","limit":"20"}
        payload = "providing the currently requested pagination and sorting parameters"
        headers = {'Accept': "application/json",'Content-Type': "application/json",'Cache-Control': "no-cache"}
        # first obtain a valid token by calling login_vra_token
        theToken = self.login_vra_token(url+"/identity/api/tokens",user,pwd,tenant)
        
        if theToken != None:
            headers = {'Accept': "application/json",'Authorization': "Bearer " + theToken,'Cache-Control': "no-cache"}
            response = requests.request("GET", url+"/component-registry/services", data=payload, headers=headers, params=querystring, verify=False)
            if response:

               #print("DEBUG OK - Obtained vRA Registered Services response \n")
               servicesJSON = json.loads(response.content.decode('utf-8'))
               #print("DEBUG OK - parsed services into JSON format \n")
               return servicesJSON['content']
            else:
               #print("DEBUG, PROBLEM: failed to obtain vRA Registered Services!")
               #return response
               raise Exception("Failed to obtain vRA registered Services for tenant: " + tenant)
        else:
            #print("DEBUG, PROBLEM: vRA login failed - cannot retrieve services data!")
            return None

    #end of get_registered_services function definition

    #start Test suite method 'check_registered_services' definition 
    @test_name("Check number of vRA Registered services")
    @test_description("Checks that core vRA Services are Registered Post Upgrade")
    @test_access_level(AccessLevel.NORMAL.value)
    @test_severity(Severity.NORMAL.value)
    @test_remediation("https://docs.vmware.com/en/vRealize-Automation/7.5/com.vmware.vra.install.upgrade.doc/GUID-6A8CFE2E-4685-48AF-BC4E-20F816C46A21.html?hWord=N4IghgNiBcIG4CUCCACATgUwOYEsDOALhpgCYp7Fw4DGGeIAvkA")
    @test
    def check_registered_services(self,vraaddress,vrausername,vrapassword,vratenant,numservices):
	                              
        #invoke class function get_registered_services with 
        servicesJSON = self.get_registered_services(vraaddress,vrausername,vrapassword,vratenant)

        if servicesJSON:
            
            #print("Asserting length of all registered vRA services >= "+str(numservices)+" - " +str(len(servicesJSON)>=int(numservices)))
            assert len(servicesJSON) >= int(numservices), "Number of registered vRA services: "+ str(len(servicesJSON))+ " is less than expected: " + str(numservices)
            
        else:
            #if NULL - return false
            #print("No registered vRA services were retrieved - FAILED HEALTH TEST!")
            assert False, "vRA Registered Services were not retrieved - FAILING HEALTH TEST!"

        return True
    #end of Test suite method 'check_registered_services' definition
	
    #Start function definition to obtain distinct endpoint types in vRA tenant
    def get_distinct_endpoint_types(self,url,user,pwd,tenant):
         
         #first, login to VRA specific tenant identified by 'tenant'
         theToken = self.login_vra_token(url + "/identity/api/tokens", user, pwd, tenant)
         
         if theToken != None:
             headers = {'Accept': "application/json", 'Authorization': "Bearer " + theToken,'Cache-Control': "no-cache"}
             querystring = {"page": "1", "limit": "20"}
             response = requests.request("GET", url+"/component-registry/endpoints/types", headers=headers, params=querystring, verify=False)
             if response:
                 #print("DEBUG SO FAR OK - Obtained vRA Distinct Endpoint types response \n")
                 # servicesJSON = json.loads(response.content)
                 endpointsJSON = json.loads(response.content.decode('utf-8'))
                 #print("DEBUG OK - parsed Distinct Endpoint types into JSON format! \n")
                 return endpointsJSON['content']
             else:
                 #print("DEBUG, PROBLEM: failed to obtain Distinct Endpoint types!")
                 #return response
                 raise Exception("Failed to obtain distinct vRA Endpoint types for tenant: "+tenant)

         else:
             #print("DEBUG, PROBLEM: vRA login failed - cannot retrieve distinct Endpoints data!")
             return None

    #end function definition to obtain distinct endpoint types in vRA tenant

    #start Test suite method 'check_distinct_endpoints' definition
    @test_name("Check number of vRA Distinct Endpoints")
    @test_description("Checks that expected number of Distinct vRA Endpoints is available")
    @test_access_level(AccessLevel.NORMAL.value)
    @test_severity(Severity.NORMAL.value)
    @test_remediation("https://docs.vmware.com/en/vRealize-Automation/7.5/com.vmware.vra.prepare.use.doc/GUID-5B87344A-F9AD-4AD2-A7A7-B8C34074E59E.html?hWord=N4IghgNiBcIG4CcCmkCWAvJACJA7AJgA4D2quALiAL5A")
    @test
    def check_distinct_endpoints(self, vraaddress, vrausername, vrapassword, vratenant, numendpoints):
        
        endpointsJSON = self.get_distinct_endpoint_types(vraaddress, vrausername, vrapassword, vratenant)

        if endpointsJSON:
            #print("Asserting length of all Distinct VRA endpoints >= " + str(numendpoints) + " - " + str(len(endpointsJSON) >= int(numendpoints)))
            assert len(endpointsJSON) >= int(numendpoints), "Number of Distinct vRA endpoints: " + str(len(endpointsJSON)) + " is less than expected: " + str(numendpoints)

        else:
            #print("No distinct VRA endpoints were retrieved - FAILED HEALTH TEST!")
            assert False, "Distinct vRA endpoints were not retrieved - FAILING HEALTH TEST!"

        return True
    #end of Test suite method 'check_distinct_endpoints'	
	
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++
    # start function defintion to get distinct Reservation types from non default vRA Tenant
    def get_reservation_types(self,url,user,pwd,tenant):
        
        theToken = self.login_vra_token(url + "/identity/api/tokens", user, pwd, tenant)
        
        if theToken != None:
            
            headers = {'Accept': "application/json", 'Authorization': "Bearer " + theToken, 'Cache-Control': "no-cache"}
            querystring = {"page": "1", "limit": "20"}
            response = requests.request("GET", url + "/reservation-service/api/reservations/types", headers=headers, params=querystring, verify=False)
            if response:

                #print("DEBUG OK - Obtained vRA Reservation types response \n")
                restypesJSON = json.loads(response.content.decode('utf-8'))
                #print("DEBUG OK - parsed Distinct vRA Reservation types into JSON format \n")
                return restypesJSON['content']
            else:
                #print("DEBUG, PROBLEM: failed to obtain vRA Distinct Reservation types!") 
                #return response
                raise Exception("Failed to obtain vRA reservation types for tenant: " + tenant)
        else:
            #print("DEBUG, PROBLEM: vRA login failed - cannot retrieve vRA Reservation data!")
            return None
    #end function to get distinct Reservation types from non default vRA Tenant
	
    # start Test suite method 'check_distinct_reservation_types' definition
    @test_name("Check number of vRA Distinct Reservation Types in a Tenant")
    @test_description("Checks that expected number of Reservation Types in a Tenant is present")
    @test_access_level(AccessLevel.NORMAL.value)
    @test_severity(Severity.NORMAL.value)
    @test_remediation("https://docs.vmware.com/en/vRealize-Automation/7.5/com.vmware.vra.prepare.use.doc/GUID-7F97AB08-7C2F-4462-AE9F-2B39C00F0E39.html?hWord=N4IghgNiBcIG4CcCmkCWAvJACZBnJCcYALqgPYB2IAvkA")
    @test
    def check_distinct_reservation_types(self, vraaddress, vratenantusername, vratenantpassword, vranondeftenant,numrestypes):
        
        restypesJSON = self.get_reservation_types(vraaddress, vratenantusername, vratenantpassword, vranondeftenant)
        if restypesJSON:
            #print("Asserting length of all distinct vRA Reserv types >= " + str(numrestypes) + " - " + str(len(restypesJSON) >= int(numrestypes)))
            assert len(restypesJSON) >= int(numrestypes), "Number of distinct tenant vRA Reservation types: " + str(len(restypesJSON)) + "  less than expected: " + str(numrestypes)
            
        else:
            #if NULL - return false
            #print("No distinct vRA Reservation types were retrieved - FAILED HEALTH TEST!")
            assert False, "Distinct vRA Reservation types were not retrieved - FAILING HEALTH TEST!"

        return True
    #end of Test method check_distinct_reservation_types	

################################################################################################
#
# Test Suite Execution
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
        suite = vRAUpgradeTestSuite()
        suite.register_tests_with_framework(host, token, modulename, venv)
