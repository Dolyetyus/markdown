import unittest
import xml.etree.ElementTree as etree
from markdown.extensions.codehilite import HiliteTreeprocessor as HT
from markdown.core import Markdown
from markdown.coverage_tracker import branch_coverage_HT

def print_coverage(branch_coverage: dict) -> None:
    hit_count = sum(hit for hit in branch_coverage.values())
    total_branches = len(branch_coverage)
    coverage_percentage = (hit_count / total_branches) * 100 if total_branches > 0 else 0
    
    for branch, hit in branch_coverage.items():
        print(f"\"{branch}\" flag: {'on' if hit else 'off'}")
    
    print("Total function coverage: {:.2f}%".format(coverage_percentage))

def clear_coverage(branch_coverage: dict) -> None:
    for branch in branch_coverage.keys():
        branch_coverage[branch] = False


class TestHTRun(unittest.TestCase):
    
    test_md = Markdown()
    test_HT_obj = HT(test_md)
    test_HT_obj.config = dict()
    
    def test_empty_coverage(self):
        print("-" * 10 + "HT.run Coverage")
        print("-" * 5 + "no flags on")
        print_coverage(branch_coverage_HT)
    
    def test_first_flag(self):
        print("-" * 5 + "first flag on")
        root = etree.fromstring("<pre>test</pre>")
        self.test_HT_obj.run(root)
        print_coverage(branch_coverage_HT)
        clear_coverage(branch_coverage_HT)

    def test_first_second_flags(self):
        print("-" * 5 + "first + second flags on")
        root = etree.fromstring("""<pre><code>print("Hello World")</code></pre>""")
        self.test_HT_obj.run(root)
        print_coverage(branch_coverage_HT)
        clear_coverage(branch_coverage_HT)
    
    def test_first_second_third_flags(self):
        print("-" * 5 + "first + second + third flags on")
        root = etree.fromstring("""<pre><code></code></pre>""")
        self.test_HT_obj.run(root)
        print_coverage(branch_coverage_HT)
        clear_coverage(branch_coverage_HT)
   
if __name__ == '__main__':
    print("-" * 3 + "HT.run Coverage Without Included Tests" + "-" * 3)
    print_coverage(branch_coverage_HT)
    unittest.main()
