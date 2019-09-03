""" A test task for Arseny Gaevsky """
# Steps to implement
# 1 Create 2 programs via rest
# 2 Open the 1st program info panel
# 3 Map the 2nd program as a Child program (click on Add tab, click on Child programs, choose needed program as child and click on Map Selected button)
# 4 Confirm mapping on the Confirmation modal
# 5 Check that Child Programs tab appears with mapped programs and tab number is updated



# http://localhost:8080/api/programs
# POST
# [{"program":{"status":"Draft","send_by_default":true,"recipients":"Admin,Primary Contacts,Secondary Contacts","custom_attribute_definitions":[],"custom_attribute_values":[],"access_control_list":[{"ac_role_id":1333,"person":{"type":"Person","id":2}}],"kind":"Directive","title":"test03","slug":"","-1":3,"context":{"id":null}}}]

import pytest
from lib import base, url
from lib.constants import locator
from lib.entities import entities_factory
from lib.utils import selenium_utils

import test.selenium.src.lib.rest.api_client

class TestAGaevskyTask(base.Test):
  """ *** """

  def test_my_scenario(self):
    """ *** """
    pass
