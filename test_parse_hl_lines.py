import unittest
from markdown.extensions.codehilite import parse_hl_lines
from markdown.coverage_tracker import branch_coverage_hl

class TestParseHlLines(unittest.TestCase):
    def coverage_before_tests(self):
        print("-"*3 + "parse_hl_lines Coverage Without Included Tests" + "-"*3)
        print_coverage(branch_coverage_hl)

    #@unittest.skip("Tests added are skipped to show")
    def test_empty_string(self):
        """Test that an empty string returns an empty list."""
        result = parse_hl_lines("")
        self.assertEqual(result, [])
        self.assertTrue(branch_coverage_hl["parse_hl_lines_10"])

        print("-"*10 + "parse_hl_lines Test 1" + "-"*10)
        print_coverage(branch_coverage_hl)

    #@unittest.skip("Tests added are skipped to show")
    def test_invalid_line_number(self):
        """ Should normally throw ValueError."""
        result = parse_hl_lines("1 a 3")
        self.assertEqual(result, [])
        self.assertTrue(branch_coverage_hl["parse_hl_lines_12"])

        print("-"*10 + "parse_hl_lines Test 2" + "-"*10)
        print_coverage(branch_coverage_hl)

    #@unittest.skip("Tests added are skipped to show")
    def test_valid_line_numbers(self):
        """Test that valid line numbers are returned as a list of integers."""
        result = parse_hl_lines("1 2 3")
        self.assertEqual(result, [1, 2, 3])
        self.assertTrue(branch_coverage_hl["parse_hl_lines_11"])

        print("-"*10 + "parse_hl_lines Test 3" + "-"*10)
        print_coverage(branch_coverage_hl)


def print_coverage(branch_list):
    hit_count = sum(hit for hit in branch_list.values())
    total_branches = len(branch_list)
    coverage_percentage = (hit_count / total_branches) * 100 if total_branches > 0 else 0
    
    for branch, hit in branch_list.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
    
    print("Total function coverage: {:.2f}%".format(coverage_percentage))


if __name__ == '__main__':
    unittest.main()

