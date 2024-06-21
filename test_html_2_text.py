import unittest
from markdown.extensions.toc import stashedHTML2text
from markdown.coverage_tracker import branch_coverage_html_2_text
from test_HT_run import print_coverage, clear_coverage

class TestHTML2Text(unittest.TestCase):

    def test_empty_coverage(self):
        print("-" * 10 + "html_2_text Coverage")
        print("-" * 5 + "no flags on")
        print_coverage(branch_coverage_html_2_text)