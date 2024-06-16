import unittest
from lxml import etree
from markdown.util import AtomicString
from markdown.extensions.toc import get_name
from markdown.coverage_tracker import branch_coverage_get_name


class TestGetName(unittest.TestCase):

    def test_get_name_with_atomic_string(self):
        el = etree.Element("title")
        el.text = AtomicString("Important Title")
        result = get_name(el)
        self.assertEqual(result, "Important Title")
        self.assertTrue(branch_coverage_get_name["get_name_31"])
        print_coverage(branch_coverage_get_name)

    def test_get_name_with_text(self):
        el = etree.Element("title")
        el.text = "Hello, World!"
        result = get_name(el)
        self.assertEqual(result, "Hello, World!")
        self.assertTrue(branch_coverage_get_name["get_name_31"])
        print_coverage(branch_coverage_get_name)


def print_coverage(branch_list):
    hit_count = sum(hit for hit in branch_list.values())
    total_branches = len(branch_list)
    coverage_percentage = (hit_count / total_branches) * 100 if total_branches > 0 else 0

    for branch, hit in branch_list.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

    print("Total function coverage: {:.2f}%".format(coverage_percentage))


if __name__ == '__main__':
    print_coverage(branch_coverage_get_name)
    # Run the tests
    unittest.main()


