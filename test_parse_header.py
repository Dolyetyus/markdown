import unittest
from markdown.extensions.codehilite import CodeHilite
from markdown.coverage_tracker import branch_coverage_parse_header
from test_dequote import print_coverage

class TestParseHeader(unittest.TestCase):

    def setUp(self):
        print("\n" + "-" * 3 + f"Starting {self._testMethodName}" + "-" * 3)

    def tearDown(self):
        print_coverage(branch_coverage_parse_header)
        print("-" * 20)

    def test_real_shebang(self):
        block = CodeHilite("#!/usr/bin/python\nprint('Hello')")
        block._parseHeader()
        self.assertEqual(block.lang, 'python')
        self.assertTrue(branch_coverage_parse_header["parse_header_32"])
        self.assertTrue(branch_coverage_parse_header["parse_header_33"])
        self.assertTrue(branch_coverage_parse_header["parse_header_34"])
        self.assertTrue(branch_coverage_parse_header["parse_header_35"])


    def test_mock_shebang(self):
        block = CodeHilite("#!python\nprint('Hello')")
        block._parseHeader()
        self.assertEqual(block.lang, 'python')
        self.assertTrue(branch_coverage_parse_header["parse_header_32"])
        self.assertFalse(branch_coverage_parse_header["parse_header_33"])
        self.assertTrue(branch_coverage_parse_header["parse_header_34"])
        self.assertTrue(branch_coverage_parse_header["parse_header_35"])

    def test_mock_colons(self):
        block = CodeHilite(":::python\nprint('Hello')")
        block._parseHeader()
        self.assertEqual(block.lang, 'python')
        self.assertTrue(branch_coverage_parse_header["parse_header_32"])
        self.assertFalse(branch_coverage_parse_header["parse_header_33"])
        self.assertFalse(branch_coverage_parse_header["parse_header_34"])
        self.assertTrue(branch_coverage_parse_header["parse_header_35"])

    def test_highlight_lines(self):
        block = CodeHilite(":::python hl_lines=\"1 3\"\nprint('Hello')")
        block._parseHeader()
        self.assertEqual(block.lang, 'python')
        self.assertEqual(block.options['hl_lines'], [1, 3])
        self.assertTrue(branch_coverage_parse_header["parse_header_32"])
        self.assertFalse(branch_coverage_parse_header["parse_header_33"])
        self.assertFalse(branch_coverage_parse_header["parse_header_34"])
        self.assertTrue(branch_coverage_parse_header["parse_header_35"])


    def test_no_match(self):
        block = CodeHilite("print('Hello')")
        block._parseHeader()
        self.assertIsNone(block.lang)
        self.assertTrue(branch_coverage_parse_header["parse_header_36"])


if __name__ == '__main__':
    unittest.main()
