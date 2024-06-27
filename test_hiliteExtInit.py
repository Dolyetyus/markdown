import unittest

from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.coverage_tracker import branch_coverage_hiliteExtInit
from test_hiliteInit import print_coverage

std_config = {
            'linenums': [
                None, "Use lines numbers. True|table|inline=yes, False=no, None=auto. Default: `None`."
            ],
            'guess_lang': [
                True, "Automatic language detection - Default: `True`."
            ],
            'css_class': [
                "codehilite", "Set class name for wrapper <div> - Default: `codehilite`."
            ],
            'pygments_style': [
                'default', 'Pygments HTML Formatter Style (Colorscheme). Default: `default`.'
            ],
            'noclasses': [
                False, 'Use inline styles instead of CSS classes - Default `False`.'
            ],
            'use_pygments': [
                True, 'Highlight code blocks with pygments. Disable if using a JavaScript library. Default: `True`.'
            ],
            'lang_prefix': [
                'language-', 'Prefix prepended to the language when `use_pygments` is false. Default: `language-`.'
            ],
            'pygments_formatter': [
                'html', 'Use a specific formatter for Pygments highlighting. Default: `html`.'
            ],
        }

class testInit(unittest.TestCase):
    #@unittest.skip("Tests added are skipped to show")
    def test_a_no_args(self):
        print("-"*10 + "Test 1" + "-"*10)
        code = CodeHiliteExtension()
        self.assertFalse(branch_coverage_hiliteExtInit["codehilite_initExt_43"])
        assert code.config == std_config
        print_coverage(branch_coverage_hiliteExtInit)
    
    #@unittest.skip("Tests added are skipped to show")   
    def test_b_key_in_config(self):
        print("-"*10 + "Test 2" + "-"*10)
        code = CodeHiliteExtension(linenums = 'False', use_pygments = 'False')
        self.assertTrue(branch_coverage_hiliteExtInit["codehilite_initExt_43"])
        self.assertTrue(branch_coverage_hiliteExtInit["codehilite_initExt_44"])
        assert code.config['linenums'] == [False, 'Use lines numbers. True|table|inline=yes, False=no, None=auto. Default: `None`.']
        assert code.config['use_pygments'] == [False, 'Highlight code blocks with pygments. Disable if using a JavaScript library. Default: `True`.']
        print_coverage(branch_coverage_hiliteExtInit)
        
    #@unittest.skip("Tests added are skipped to show")
    def test_c_key_not_in_config_and_not_string(self):
        print("-"*10 + "Test 3" + "-"*10)
        code = CodeHiliteExtension(not_string = 34)
        self.assertTrue(branch_coverage_hiliteExtInit["codehilite_initExt_43"])
        self.assertTrue(branch_coverage_hiliteExtInit["codehilite_initExt_45"])
        self.assertFalse(branch_coverage_hiliteExtInit["codehilite_initExt_46"])
        #print(code.config['not_string'])
        assert code.config['not_string'] == [34, '']
        print_coverage(branch_coverage_hiliteExtInit)
        
    #@unittest.skip("Tests added are skipped to show")
    def test_d_key_not_in_config_but_string(self):
        print("-"*10 + "Test 4" + "-"*10)
        code = CodeHiliteExtension(unknown = 'True', CJ = 'Follow the train')
        self.assertTrue(branch_coverage_hiliteExtInit["codehilite_initExt_43"])
        self.assertTrue(branch_coverage_hiliteExtInit["codehilite_initExt_45"])
        self.assertTrue(branch_coverage_hiliteExtInit["codehilite_initExt_46"])
        assert code.config['unknown'] == [True, '']
        assert code.config['CJ'] == ['Follow the train', '']
        print_coverage(branch_coverage_hiliteExtInit)
        
    @unittest.skip("Tests added are skipped to show")
    def test_A_no_coverage(self):
        print("-"*10 + "Test 0(no_coverage)" + "-"*10)
        print_coverage(branch_coverage_hiliteExtInit)

    
if __name__ == '__main__':
    unittest.main()   