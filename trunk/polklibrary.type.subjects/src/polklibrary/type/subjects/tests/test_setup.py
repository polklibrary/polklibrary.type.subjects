# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from polklibrary.type.subjects.testing import POLKLIBRARY_TYPE_SUBJECTS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that polklibrary.type.subjects is properly installed."""

    layer = POLKLIBRARY_TYPE_SUBJECTS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if polklibrary.type.subjects is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('polklibrary.type.subjects'))

    def test_browserlayer(self):
        """Test that IPolklibraryTypeSubjectsLayer is registered."""
        from polklibrary.type.subjects.interfaces import IPolklibraryTypeSubjectsLayer
        from plone.browserlayer import utils
        self.assertIn(IPolklibraryTypeSubjectsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLKLIBRARY_TYPE_SUBJECTS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['polklibrary.type.subjects'])

    def test_product_uninstalled(self):
        """Test if polklibrary.type.subjects is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('polklibrary.type.subjects'))

    def test_browserlayer_removed(self):
        """Test that IPolklibraryTypeSubjectsLayer is removed."""
        from polklibrary.type.subjects.interfaces import IPolklibraryTypeSubjectsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPolklibraryTypeSubjectsLayer, utils.registered_layers())
