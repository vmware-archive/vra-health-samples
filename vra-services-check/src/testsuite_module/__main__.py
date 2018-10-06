""" 
vRA Post Upgrade Health Test Implementation Module Main

Copyright © 2017-2018 VMware, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the “License”); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at http://www.apache.org/licenses/LICENSE-2.0
  
Some files may be comprised of various open source software components, each of which
has its own license that is located in the source code of the respective component.
"""
import sys
#import vRAUpgradeTestSuite test suite source
from testsuite_module.vrahealthtestsuite import vRAUpgradeTestSuite

#print("Executing Suite of vRA Post Updgrade Tests with " + str(sys.argv))
#initialize and execute vRAUpgradeTestSuite
suite = vRAUpgradeTestSuite()
suite.run_tests(*sys.argv)
