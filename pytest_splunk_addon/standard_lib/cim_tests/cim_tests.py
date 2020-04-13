# -*- coding: utf-8 -*-
"""
Includes the test scenarios to check the CIM compatibility of an Add-on.
"""

import logging

class CIMTests:
    """
    Test scenarios to check the CIM compatibility of an Add-on 
    Supported Test scenarios:
        - The eventtype should exctract all required fields of data model 
        - One eventtype should not be mapped with more than one data model 
        - Field Cluster should be verified (should be included with required field test)
        - Verify if CIM installed or not 
        - TODO 
    """
    logger = logging.getLogger("pytest-splunk-addon-cim-tests")

    # TODO: Add Test scenarios 
