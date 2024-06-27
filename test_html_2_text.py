import unittest
from markdown.extensions.toc import stashedHTML2text
from markdown.core import Markdown
from markdown.util import STX, ETX
from markdown.coverage_tracker import branch_coverage_html_2_text
from test_HT_run import print_coverage, clear_coverage

class TestHTML2Text(unittest.TestCase):
    
    test_md = Markdown()
    test_md.htmlStash.rawHtmlBlocks += "test"
    
    def test_empty_coverage(self):
        print("-" * 10 + "html_2_text Coverage")
        print("-" * 5 + "no flags on")
        print_coverage(branch_coverage_html_2_text)
    
    def test_first_flag_on(self):
        print("-" * 5 + "first flag on")
        stashedHTML2text(STX + "wzxhzdk:0" + ETX + "testing" + STX + "wzxhzdk:1" + ETX, self.test_md, False)
        print_coverage(branch_coverage_html_2_text)
        clear_coverage(branch_coverage_html_2_text)

    def test_first_second_flags_on(self):
        print("-" * 5 + "first + second flags on")
        stashedHTML2text(STX + "wzxhzdk:0" + ETX + "testing" + STX + "wzxhzdk:1" + ETX, self.test_md)
        print_coverage(branch_coverage_html_2_text)
        clear_coverage(branch_coverage_html_2_text)

if __name__ == '__main__':
    print("-" * 3 + "html_2_text Coverage Without Included Tests" + "-" * 3)
    print_coverage(branch_coverage_html_2_text)
    unittest.main()