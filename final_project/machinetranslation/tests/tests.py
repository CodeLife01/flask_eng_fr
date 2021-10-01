#!/usr/bin/env python3
# Author : Arthur Thouvenin
# Contact : athouvenin [at] outlook.fr
# Created : 09/09/2021
# Last update : 09/09/2021
"""
This is the presentation of the module

"""

import unittest
from translator import english_to_french, french_to_english

class TestTranslateEnToFr(unittest.TestCase):
    """
    Class to test the function english_to_french
    """
    def test1(self):
        """
        Function to test the function english_to_french
        """
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

class TestTranslateFrToEn(unittest.TestCase):
    """
    Class to test the function french_to_english
    """
    def test1(self):
        """
        Function to test the function french_to_english
        """
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")

unittest.main()
