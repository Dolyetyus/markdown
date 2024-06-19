import unittest
from markdown.inlinepatterns import dequote
from markdown.coverage_tracker import branch_coverage_dequote


class AtomicString(str):
    pass

class TestGetName(unittest.TestCase):
    def test_dequote_with_double_quotes(self):
        result = dequote('"Hello"')
        self.assertEqual(result, 'Hello')
        self.assertTrue(branch_coverage_dequote["dequote_30"])
        print_coverage(branch_coverage_dequote)


    def test_dequote_with_single_quotes(self):
        result = dequote("'World'")
        self.assertEqual(result, 'World')
        self.assertTrue(branch_coverage_dequote["dequote_30"])
        print_coverage(branch_coverage_dequote)


    def test_dequote_with_no_quotes(self):
        result = dequote('Hello World')
        self.assertEqual(result, 'Hello World')
        self.assertTrue(branch_coverage_dequote["dequote_31"])
        print_coverage(branch_coverage_dequote)


def print_coverage(branch_list):
    hit_count = sum(hit for hit in branch_list.values())
    total_branches = len(branch_list)
    coverage_percentage = (hit_count / total_branches) * 100 if total_branches > 0 else 0

    for branch, hit in branch_list.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

    print("Total function coverage: {:.2f}%".format(coverage_percentage))

if __name__ == '__main__':
    # Print the contents of branch_coverage_dequote
    print(print_coverage(branch_coverage_dequote))

    # Calculate and print function coverage
    print_coverage(branch_coverage_dequote)
    unittest.main()
