import unittest
from markdown.extensions.codehilite import CodeHilite
from unittest.mock import patch, MagicMock
from markdown.coverage_tracker import branch_coverage_cd
from test_parse_hl_lines import print_coverage

class OrderedTestSuite(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        test_methods = [
            TestCodeHilite.test_hilite_with_language,
            TestCodeHilite.test_hilite_guess_language,
            TestCodeHilite.test_hilite_no_pygments_with_line_numbers,
            TestCodeHilite.test_hilite_with_invalid_formatter,
            TestCodeHilite.test_hilite_with_linenos,
            TestCodeHilite.test_hilite_without_shebang,
            TestCodeHilite.test_hilite_with_custom_formatter,
            TestCodeHilite.test_hilite_with_double_fallback,
            TestCodeHilite.test_hilite_no_pygments_with_classes
        ]
        for method in test_methods:
            self.addTest(method())

class TestCodeHilite(unittest.TestCase):

    def coverage_before_tests_hl(self):
        print("-"*3 + "hilite Coverage Without Included Tests" + "-"*3)
        print_coverage(branch_coverage_cd)

    @patch('markdown.extensions.codehilite.get_lexer_by_name')
    @patch('markdown.extensions.codehilite.highlight')
    def test_hilite_with_language(self, mock_highlight, mock_get_lexer):
        """Test hilite with specified language."""
        code = CodeHilite('print("Hello, World!")', lang='python')

        mock_get_lexer.return_value = 'mocked_lexer'
        mock_highlight.return_value = '<div>highlighted_code</div>'

        result = code.hilite()

        self.assertIn('highlighted_code', result)
        self.assertTrue(branch_coverage_cd["hilite_14"])
        self.assertTrue(branch_coverage_cd["hilite_15"])
        self.assertTrue(branch_coverage_cd["hilite_22"])
        self.assertTrue(branch_coverage_cd["hilite_23"])

        print("-"*10 + "hilite Test 1" + "-"*10)
        print_coverage(branch_coverage_cd)

    @patch('markdown.extensions.codehilite.get_lexer_by_name')
    @patch('markdown.extensions.codehilite.guess_lexer')
    @patch('markdown.extensions.codehilite.highlight')
    def test_hilite_guess_language(self, mock_highlight, mock_guess_lexer, mock_get_lexer):
        """Test hilite with language guessing."""
        code = CodeHilite('print("Hello, World!")', lang=None, guess_lang=True)

        mock_get_lexer.side_effect = ValueError
        mock_guess_lexer.return_value = MagicMock(aliases=['python'])
        mock_highlight.return_value = '<div>highlighted_code</div>'

        result = code.hilite()

        self.assertIn('highlighted_code', result)
        self.assertTrue(branch_coverage_cd["hilite_18"])
        self.assertTrue(branch_coverage_cd["hilite_21"])

        print("-" * 10 + "hilite Test 2" + "-" * 10)
        print_coverage(branch_coverage_cd)

    @patch('markdown.extensions.codehilite.get_lexer_by_name')
    @patch('markdown.extensions.codehilite.highlight')
    def test_hilite_no_pygments_with_line_numbers(self, mock_highlight, mock_get_lexer):
        """Test hilite without pygments (JavaScript fallback) with line numbers."""
        code = CodeHilite('print("Hello, World!")', use_pygments=False, linenos=True)

        result = code.hilite()

        self.assertIn('<pre class="codehilite"><code class="linenums">', result)
        self.assertIn('print(&quot;Hello, World!&quot;)', result)
        self.assertTrue(branch_coverage_cd["hilite_26"])
        self.assertTrue(branch_coverage_cd["hilite_27"])

        print("-" * 10 + "hilite Test 3" + "-" * 10)
        print_coverage(branch_coverage_cd)

    @patch('markdown.extensions.codehilite.get_lexer_by_name')
    @patch('markdown.extensions.codehilite.highlight')
    def test_hilite_with_invalid_formatter(self, mock_highlight, mock_get_lexer):
        """Test hilite with invalid pygments formatter."""
        code = CodeHilite('print("Hello, World!")', lang='python', pygments_formatter='invalid_formatter')

        mock_get_lexer.return_value = 'mocked_lexer'
        mock_highlight.return_value = '<div>highlighted_code</div>'

        result = code.hilite()

        self.assertIn('highlighted_code', result)
        self.assertTrue(branch_coverage_cd["hilite_24"])

        print("-" * 10 + "hilite Test 4" + "-" * 10)
        print_coverage(branch_coverage_cd)

    @patch('markdown.extensions.codehilite.get_lexer_by_name')
    @patch('markdown.extensions.codehilite.highlight')
    def test_hilite_with_linenos(self, mock_highlight, mock_get_lexer):
        """Test hilite with line numbers enabled."""
        code = CodeHilite('print("Hello, World!")', lang='python', linenums=True)

        mock_get_lexer.return_value = 'mocked_lexer'
        mock_highlight.return_value = '<div>highlighted_code</div>'

        result = code.hilite()

        self.assertIn('highlighted_code', result)
        self.assertTrue(branch_coverage_cd["hilite_14"])
        self.assertTrue(branch_coverage_cd["hilite_27"])

        print("-" * 10 + "hilite Test 5" + "-" * 10)
        print_coverage(branch_coverage_cd)

    def test_hilite_without_shebang(self):
        """Test hilite without shebang parsing."""
        code = CodeHilite('print("Hello, World!")', lang=None)

        result = code.hilite(shebang=False)

        self.assertNotIn('<span class="k">', result)
        self.assertTrue(branch_coverage_cd["hilite_14"])

        print("-"*10 + "hilite Test 6" + "-"*10)
        print_coverage(branch_coverage_cd)

    @patch('markdown.extensions.codehilite.get_lexer_by_name')
    @patch('markdown.extensions.codehilite.highlight')
    def test_hilite_with_custom_formatter(self, mock_highlight, mock_get_lexer):
        """Test hilite with custom pygments formatter callable."""
        def custom_formatter(lang_str, **options):
            return 'mocked_formatter'

        code = CodeHilite('print("Hello, World!")', lang='python', pygments_formatter=custom_formatter)

        mock_get_lexer.return_value = 'mocked_lexer'
        mock_highlight.return_value = '<div>highlighted_code</div>'

        result = code.hilite()

        self.assertIn('highlighted_code', result)
        self.assertTrue(branch_coverage_cd["hilite_25"])

        print("-" * 10 + "hilite Test 7" + "-" * 10)
        print_coverage(branch_coverage_cd)

    @patch('markdown.extensions.codehilite.get_lexer_by_name')
    @patch('markdown.extensions.codehilite.highlight')
    def test_hilite_with_double_fallback(self, mock_highlight, mock_get_lexer):
        """Test hilite with double fallback for lexer."""
        code = CodeHilite('print("Hello, World!")', lang=None, guess_lang=False)

        mock_get_lexer.side_effect = [ValueError, MagicMock()]
        mock_highlight.return_value = '<div>highlighted_code</div>'

        result = code.hilite()

        self.assertIn('highlighted_code', result)
        self.assertTrue(branch_coverage_cd["hilite_19"])

        print("-" * 10 + "hilite Test 8" + "-" * 10)
        print_coverage(branch_coverage_cd)

    @patch('markdown.extensions.codehilite.get_lexer_by_name')
    @patch('markdown.extensions.codehilite.highlight')
    def test_hilite_no_pygments_with_classes(self, mock_highlight, mock_get_lexer):
        """Test hilite without pygments but with language class and line numbers."""
        code = CodeHilite('print("Hello, World!")', use_pygments=False, lang='python', linenos=True)

        result = code.hilite()

        self.assertIn('<pre class="codehilite"><code class="language-python linenums">', result)
        self.assertIn('print(&quot;Hello, World!&quot;)', result)

        self.assertTrue(branch_coverage_cd["hilite_26"])
        self.assertTrue(branch_coverage_cd["hilite_27"])
        self.assertTrue(branch_coverage_cd["hilite_28"])

        print("-" * 10 + "hilite Test 9" + "-" * 10)
        print_coverage(branch_coverage_cd)

if __name__ == '__main__':
    suite = OrderedTestSuite()
    runner = unittest.TextTestRunner()
    runner.run
