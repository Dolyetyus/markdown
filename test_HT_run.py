import unittest
from markdown.extensions.codehilite import HiliteTreeprocessor as HT
from markdown.coverage_tracker import branch_coverage_HT

def print_title(main_str: str) -> None:
    print("-" * 10 + main_str + "-" * 10)

def print_coverage(branch_coverage: dict) -> None:
    hit_count = sum(hit for hit in branch_coverage.values())
    total_branches = len(branch_coverage)
    coverage_percentage = (hit_count / total_branches) * 100 if total_branches > 0 else 0
    
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
    
    print("Total function coverage: {:.2f}%".format(coverage_percentage))

class TestHTRun(unittest.TestCase):
    def test_empty_coverage(self):
        print_title("HT.run Coverage")
        print_coverage(branch_coverage_HT)

if __name__ == '__main__':
    print("-" * 3 + "HT.run Coverage Without Included Tests" + "-" * 3)
    print_coverage(branch_coverage_HT)
    unittest.main()
