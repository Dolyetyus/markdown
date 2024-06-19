import unittest
from markdown.markdown.extensions.codehilite import CodeHilite, __init__
from markdown.markdown.coverage_tracker import branch_coverage_hiliteInit

class testInit(unittest.TestCase):
    def test_no_options(self, src:str, **options):
        code = CodeHilite(src="print('Hello, World!')", options={})
        assert code.src == "print('Hello, World!')"
        assert code.options['linenos'] == None
        assert code.options['cssclass'] == 'codehilite'
        assert code.options['wrapcode'] == True
    
    #def test_no_linenos(self, src: str, **options):
     #   object = CodeHilite(src="print('Hello, World!')", options="linenums")
      #  assert object.src == "print('Hello, World!')"
       # assert object.options['linenos'] == 
        
        
def print_coverage(branch_list):
    hit_count = sum(hit for hit in branch_list.values())
    total_branches = len(branch_list)
    coverage_percentage = (hit_count / total_branches) * 100 if total_branches > 0 else 0

    for branch, hit in branch_list.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

    print("Total function coverage: {:.2f}%".format(coverage_percentage))


if __name__ == '__main__':
    print_coverage(branch_coverage_hiliteInit)
    # Run the tests
    unittest.main()       