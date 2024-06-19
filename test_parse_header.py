import unittest
from markdown.extensions.codehilite import CodeHilite
from markdown.coverage_tracker import branch_coverage_parse_header


class TestParseHeader(unittest.TestCase):

    def test_real_shebang(self):
        block = CodeHilite("#!/usr/bin/python\nprint('Hello')")
        block._parseHeader()
        self.assertEqual(block.lang, 'python')
        self.assertTrue(branch_coverage_parse_header["parse_header_32"])
        self.assertTrue(branch_coverage_parse_header["parse_header_33"])
        self.assertTrue(branch_coverage_parse_header["parse_header_34"])
        self.assertTrue(branch_coverage_parse_header["parse_header_35"])
        print_coverage(branch_coverage_parse_header)

    def test_mock_shebang(self):
        block = CodeHilite("#!python\nprint('Hello')")
        block._parseHeader()
        self.assertEqual(block.lang, 'python')
        self.assertTrue(branch_coverage_parse_header["parse_header_32"])
        self.assertFalse(branch_coverage_parse_header["parse_header_33"])
        self.assertTrue(branch_coverage_parse_header["parse_header_34"])
        self.assertTrue(branch_coverage_parse_header["parse_header_35"])
        print_coverage(branch_coverage_parse_header)


    def test_mock_colons(self):
        block = CodeHilite(":::python\nprint('Hello')")
        block._parseHeader()
        self.assertEqual(block.lang, 'python')
        self.assertTrue(branch_coverage_parse_header["parse_header_32"])
        self.assertFalse(branch_coverage_parse_header["parse_header_33"])
        self.assertFalse(branch_coverage_parse_header["parse_header_34"])
        self.assertTrue(branch_coverage_parse_header["parse_header_35"])
        print_coverage(branch_coverage_parse_header)

    def test_highlight_lines(self):
        block = CodeHilite(":::python hl_lines=\"1 3\"\nprint('Hello')")
        block._parseHeader()
        self.assertEqual(block.lang, 'python')
        self.assertEqual(block.options['hl_lines'], [1, 3])
        self.assertTrue(branch_coverage_parse_header["parse_header_32"])
        self.assertFalse(branch_coverage_parse_header["parse_header_33"])
        self.assertFalse(branch_coverage_parse_header["parse_header_34"])
        self.assertTrue(branch_coverage_parse_header["parse_header_35"])
        print_coverage(branch_coverage_parse_header)

    def test_no_match(self):
        block = CodeHilite("print('Hello')")
        block._parseHeader()
        self.assertIsNone(block.lang)
        self.assertTrue(branch_coverage_parse_header["parse_header_36"])
        print_coverage(branch_coverage_parse_header)





def print_coverage(branch_list):
    hit_count = sum(hit for hit in branch_list.values())
    total_branches = len(branch_list)
    coverage_percentage = (hit_count / total_branches) * 100 if total_branches > 0 else 0

    for branch, hit in branch_list.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

    print("Total function coverage: {:.2f}%".format(coverage_percentage))

if __name__ == '__main__':
    unittest.main(exit=False)

    print("Coverage Report:")
    print_coverage(branch_coverage_parse_header)