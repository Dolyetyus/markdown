import unittest

from markdown.extensions.codehilite import CodeHilite
from markdown.coverage_tracker import branch_coverage_hiliteInit

class testInit(unittest.TestCase):
    
    def test_d_no_options(self): 
        code = CodeHilite(src="print('Hello, World!')")
        assert code.src == "print('Hello, World!')"
        self.assertTrue(branch_coverage_hiliteInit["codehilite_init_40"])
        self.assertTrue(branch_coverage_hiliteInit["codehilite_init_41"])
        self.assertTrue(branch_coverage_hiliteInit["codehilite_init_42"])
        print_coverage(branch_coverage_hiliteInit)
        
    def test_a_no_linenos(self):
        code = CodeHilite(src="print('Hello, World!')", cssclass='class', wrapcode=False)
        assert code.src == "print('Hello, World!')"
        self.assertTrue(branch_coverage_hiliteInit["codehilite_init_40"])
        assert code.options['linenos'] == code.options.get('linenums', None) #this checks if there is indeed linenums in the dictionary, and if not return None
        assert code.options['cssclass'] == 'class'
        assert code.options['wrapcode'] == False
        print_coverage(branch_coverage_hiliteInit)
        
    def test_b_no_css(self):
        code = CodeHilite(src="print('Hello, World!')", linenos='inline', wrapcode=False)
        assert code.src == "print('Hello, World!')"
        self.assertTrue(branch_coverage_hiliteInit["codehilite_init_41"])
        assert code.options['linenos'] == 'inline'
        assert code.options['cssclass'] == code.options.get('css_class', 'codehilite')
        assert code.options['wrapcode'] == False
        print_coverage(branch_coverage_hiliteInit)

    def test_c_no_wrap(self):
        code = CodeHilite(src="print('Hello, World!')", linenos='inline', cssclass='class')
        assert code.src == "print('Hello, World!')"
        self.assertTrue(branch_coverage_hiliteInit["codehilite_init_42"])
        assert code.options['linenos'] == 'inline'
        assert code.options['wrapcode'] == True
        assert code.options['cssclass'] == 'class'
        print_coverage(branch_coverage_hiliteInit)
        
def print_coverage(branch_list):
    hit_count = sum(hit for hit in branch_list.values())
    total_branches = len(branch_list)
    coverage_percentage = (hit_count / total_branches) * 100 if total_branches > 0 else 0

    for branch, hit in branch_list.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

    print("Total function coverage: {:.2f}%".format(coverage_percentage))


if __name__ == '__main__':
    unittest.main()   