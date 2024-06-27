# Report for Assignment 1

## Project chosen

Name: Python-Markdown

URL: https://github.com/Python-Markdown/markdown

Number of lines of code and the tool used to count it: number of lines of code (nloc): 17295. </br></br>
Tested by using Lizard to count the nloc.</br>
<img src="https://i.ibb.co/Pr4ZjNc/Whats-App-Image-2024-06-07-at-01-41-00-31a65e5a.jpg" width="600"></p>

Programming language: Python

## Coverage measurement

### Existing tool

The coverage check is done with [coverage.py](https://github.com/nedbat/coveragepy). The following command is used to check the total coverage throughout the project:
```
$ coverage run -m unittest discover
```

Total function coverage was 95%:</p>
<img src="https://github.com/Dolyetyus/markdown/assets/67073431/d40bb79d-5aa0-4910-9840-a81a2ccd36f7" width="500"></p>

### Your own coverage tool

<The following is supposed to be repeated for each group member>

**Said Musab Oguz**

#### Function Name: parse_hl_lines

[Link to the patch (diff)](https://github.com/Dolyetyus/markdown/commit/d07b27274c416ae258ec3d1003a9b26a51fed749?diff=unified&w=1)

Screenshot of the coverage results:</p>
<img src="https://i.ibb.co/DCRzTGC/image.png" width="600"></p>

<Provide a screenshot of the coverage results output by the instrumentation>

#### Function Name: codehilite

[Link to the patch (diff)](https://github.com/Dolyetyus/markdown/commit/d07b27274c416ae258ec3d1003a9b26a51fed749?diff=unified&w=1)

Screenshot of the coverage results:</p>
<img src="https://github.com/Dolyetyus/markdown/assets/67073431/813c40f4-0911-4f5a-9f5b-6852bde68676" width="600"></p>

**Mihnea-Andrei Bârsan**

#### Function name: HiliteTreeprocessor.run 

[Link to the patch (diff)](https://github.com/Dolyetyus/markdown/commit/701416ad42d5470a5cb28fe74d31e16a9e329537?diff=unified&w=0)

Screenshot of the coverage results:</p>
<img src="https://i.ibb.co/Mcc43GX/ss-init-cov.jpg" alt="screenshot-of-initial-coverage" width="600"></p>

#### Function name: stashedHTML2text._html_sub

[Link to the patch (diff)](https://github.com/Dolyetyus/markdown/commit/a8ac1c3c71bfb44c8992834f880e25df08a1c830)

Screenshot of the coverage results:</p>
<img src="https://i.ibb.co/Cnw9PW4/ss-init-cov-2.jpg" alt="screenshot-of-initial-coverage" width="600"></p>

**Robert Sofroni**

#### Function name: dequote

[Link to the patch (diff)](https://github.com/Python-Markdown/markdown/commit/69a60b1e905feaabf27a46fa67fd24ba4587ab6b)


Screenshot of the coverage results:</p>
<img src="https://i.ibb.co/r6jWdBD/Screenshot-2024-06-23-034728.png" width="600"></p>

<Provide a screenshot of the coverage results output by the instrumentation>

#### Function name: _parseHeader

[Link to the patch (diff)](https://github.com/Python-Markdown/markdown/commit/a5282a1916a2b6edd4e885bcbe5cf542f8f22c00)

Screenshot of the coverage results:</p>
<img src="https://i.ibb.co/wp75qTX/Screenshot-2024-06-23-041227.png" width="600"></p>

**Alexandru-Valentin Florea**

#### Function name: CodeHilite.__init__

[Link to the patch (diff)](https://github.com/Dolyetyus/markdown/commit/269bf63be79272e5e8d8dcd7de1f611e56f37dde)

<img src="https://i.ibb.co/W0xMY1H/func1-no-Coverage.png" width="600"></p>

<Provide a screenshot of the coverage results output by the instrumentation>

#### Function name: CodeHiliteExtension.__init__

[Link to the patch (diff)](https://github.com/Dolyetyus/markdown/commit/7700edc896123977a8ddbbf859d33c34de81d6be)

<img src="https://i.ibb.co/N9Lxxfp/func2-no-Coverage.png" width="600"></p>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

**Said Musab Oguz**

#### Test: parse_hl_lines

[Link to the patch (diff) for the new test file](https://github.com/Dolyetyus/markdown/commit/f8a67f6aab90ee436302e72e8ccdba6cd3e79ba1?diff=unified&w=1)

**Old coverage result:** </p>
<img src="https://i.ibb.co/DCRzTGC/image.png" width="600"></p>

**New coverage result:** </p>
<img src="https://i.ibb.co/VS6pwKr/image.png" width="600"></p>

As can be seen from the tests, the coverage increased from 0% to 100%. There were no tests that cover this function. After adding 3 tests that check the behaviour of the function and checks the branch coverage for all 3 branches, the coverage increased. 

The new tests check the function in 3 cases:
- Tests that an empty string returns an empty list
- Tests that the function throws a ValueError
- Tests that valid line numbers are returned as a list of integers.

#### Test: codehilite

[Link to the patch (diff) for the new test file](https://github.com/Dolyetyus/markdown/commit/f8a67f6aab90ee436302e72e8ccdba6cd3e79ba1?diff=unified&w=1)

**Old coverage result:** </p>
<img src="https://github.com/Dolyetyus/markdown/assets/67073431/813c40f4-0911-4f5a-9f5b-6852bde68676" width="600"></p>

**New coverage result:** </p>
<img src="https://github.com/Dolyetyus/markdown/assets/67073431/09afba90-5145-46f5-abb5-6c16a9271731" width="600"></p>

As can be seen from the tests, the coverage increased from 0% to 100%. There were no tests that cover this function. After adding 9 tests that check the behaviour of the function and checks the branch coverage for all 9 branches, the coverage increased with each test a little more. 

The new tests check the function in 9 cases:
- Tests hilite with specified language
- Tests hilite with language guessing
- Tests hilite without pygments (JavaScript fallback) with line numbers
- Tests hilite with invalid pygments formatter
- Tests hilite with line numbers enabled
- Tests hilite without shebang parsing
- Tests hilite with custom pygments formatter callable
- Tests hilite with double fallback for lexer
- Tests hilite without pygments but with language class and line numbers

**Mihnea-Andrei Bârsan**

#### Test: HiliteTreeprocessor.run

[Link to the patch (diff) for the new test file](https://github.com/Dolyetyus/markdown/commit/496baa31b266c101e9aab726b6a3fe827f6ae203)

**Old coverage result:**</p>
<img src="https://i.ibb.co/Mcc43GX/ss-init-cov.jpg" alt="screenshot-of-initial-coverage" width="600"></p>

**New coverage result:**</p>
<img src="https://i.ibb.co/gz8WSjm/image-2024-06-26-212147612.png" alt="screenshot-of-coverage" width="600"></p>

The initial tests of the forked repository covered 0% of the function HiliteTreeprocessor.run and, after finishing the tests in test_HT_run.py, the tests of the forked repository covered 100% of the function HiliteTreeprocessor.run. Considering that HiliteTreeprocessor.run takes indirectly as input an XML element tree, the tests in test_HT_run.py cover these scenarios:
- the inputted XML element tree contains at least one &lt;pre&gt; block, but each such &lt;pre&gt; block does not contain exactly one subblock or does not contain a &lt;code&gt; subblock;
- the inputted XML element tree contains at least one &lt;pre&gt; block and at least one such &lt;pre&gt; block contains exactly one subblock and that subblock is a &lt;code&gt; subblock and this &lt;code&gt; subblock contains some text;
- the inputted XML element tree contains at least one &lt;pre&gt; block and at least one such &lt;pre&gt; block contains exactly one subblock and that subblock is a &lt;code&gt; subblock, but this &lt;code&gt; subblock contains no text.

#### Test: stashedHTML2text._html_sub

[Link to the patch (diff) for the new test file](https://github.com/Dolyetyus/markdown/commit/a084e1630a62daa547d50096e98cd7b380a95cc1)

**Old coverage result:**</p>
<img src="https://i.ibb.co/Cnw9PW4/ss-init-cov-2.jpg" alt="screenshot-of-initial-coverage" width="600"></p>

**New coverage result:**</p>
<img src="https://i.ibb.co/y5vxZcf/image-2024-06-26-230222894.png" alt="screenshot-of-coverage" width="600"></p>

After finishing the tests in test_html_2_text.py, the tests of the forked repository went from covering 0% of the function stashedHTML2text._html_sub to covering 100% of the function stashedHTML2text._html_sub. Considering that stashedHTML2text._html_sub takes indirectly as input raw HTML, the following scenarios are covered by the tests in test_html_2_text.py:
- indirectly inputted raw HTML without stripping of entities;
- indirectly inputted raw HTML with stripping of entities.

**Robert Sofroni**

#### Test: dequote

[Link to the patch (diff) for the new test file](https://github.com/Dolyetyus/markdown/commit/7052e24d922ce604245f1db560cd34c8cc1ad8ac)

**Old coverage result:** </p>
<img src="https://i.ibb.co/r6jWdBD/Screenshot-2024-06-23-034728.png" width="600"></p>

**New coverage result:** </p>
<img src="https://i.ibb.co/2N783cr/image.png" width="600"></p>

As can be seen from the tests, the coverage increased from 0% to 100%. There were no tests that covered this function. After adding 3 tests that check the behavior of the function and check the branch coverage for all 3 branches, the coverage increased. 

The new tests check the function in 3 cases:
- Tests dequote when given a text with double quotes
- Tests dequote when given a text with single quotes
- Tests dequote when given a text that has no quotes


#### Test: _parseHeader

[Link to the patch (diff) for the new test file](https://github.com/Dolyetyus/markdown/commit/7052e24d922ce604245f1db560cd34c8cc1ad8ac)

**Old coverage result:** </p>
<img src="https://i.ibb.co/wp75qTX/Screenshot-2024-06-23-041227.png" width="600"></p>

**New coverage result:** </p>
<img src="https://i.ibb.co/C7jG761/image.png" width="600"></p>
<img src="https://i.ibb.co/c2Zmh7b/image.png" width="600"></p>

As can be seen from the tests, the coverage increased from 0% to 100%. There were no tests that covered this function. After adding 4 tests that check the behavior of the function and check the branch coverage for all 5 branches, the coverage increased with each test a little more. 

The new tests check the function in 5 cases:
- Tests _parseHeader when given a real shebang line at the beginning of the code block
- Tests _parseHeader when given a mock shebang line without a path
- Tests _parseHeader when given colons instead of a shebang line to indicate the language
- Tests _parseHeader when given a shebang-like line with highlight lines specified
- Tests _parseHeader that has no shebang or colon line at the beginning of the code block

**Alexandru-Valentin Florea**

#### Test: CodeHilite.__init__

[Link to the patch (diff)](https://github.com/Dolyetyus/markdown/commit/2e50eaa85cbf09d070186505c287855440226f93)

**Old coverage result:** </p>
<img src="https://i.ibb.co/W0xMY1H/func1-no-Coverage.png" width="600"></p>

**New coverage result:** </p>
<img src="https://i.ibb.co/0Y76LsW/func1-coverage.png" width="600"></p>

As the above screenshots show, the coverage increased from 0% to 100%. There were no tests that covered this initialisation function. After adding 4 tests that check the behaviour of the function and checks the branch coverage for all 3 branches, the coverage increased.

The tests added cover the following scenarios:
- Test a checks correct behavior with missing 'linenos' key in the arguments list
- Test b checks correct behavior with missing 'css' key in the arguments list
- Test c checks correct behavior with missing 'wrap' key in the arguments list
- Test d checks correct behavior with an empty arguments list to see if the fallback values are applied correctly
- Test A is just to show the original coverage, 0%

#### Test: CodeHiliteExtension.__init__

[Link to the patch (diff)](https://github.com/Dolyetyus/markdown/commit/f1b55e565c0ee093a67782e10ac1568dcf0b095e)

**Old coverage result:** </p>
<img src="https://i.ibb.co/N9Lxxfp/func2-no-Coverage.png" width="600"></p>

**New coverage result:** </p>
<img src="https://i.ibb.co/w4p1wKG/func2-coverage.png" width="600"></p>

As the above screenshots show, the coverage increased from 0% to 100%. There were no tests that covered this initialisation function. After adding 4 tests that check the behaviour of the function and checks the branch coverage for all 4 branches, the coverage increased.

The tests added cover the following scenarios:
- Test a checks correct behavior with empty config list, to see if the standard one is applied correctly
- Test b checks correct behavior with a key that changes a value from default config 
- Test c checks correct behavior with a key that isn't part of the original config dictionary and also isn't a string so it can't be passed to the parsing function
- Test d checks correct behavior with 
    - 1. a key that isn't part of the original config dictionary, is a string and can be parsed into a bool
    - 2. a key that isn't part of the original config dictionary, is a string but can't be parsed into a bool
- Test A is just to show the original coverage, 0%

### Overall

**The old coverage results by running the existing tool (coverage.py):** </p>
<img src="https://github.com/Dolyetyus/markdown/assets/67073431/d40bb79d-5aa0-4910-9840-a81a2ccd36f7" width="500"></p>

**The new coverage results by running the existing tool using all test modifications made by the group:** </p>
<img src="https://github.com/Dolyetyus/markdown/assets/67073431/b9dc9004-f926-4e5a-bd27-cf366c81beff" width="500"></p>

## Statement of individual contributions

#### Said Musab Oguz
- forked the upstream Python markdown repository
- added some tests for parse_hl_lines and codehilite functions
- initialized and added some parts for parse_hl_lines and codehilite functions to this README file

#### Mihnea-Andrei Bârsan
- added some tests for HiliteTreeprocessor.run and stashedHTML2text._html_sub functions
- added some parts for HiliteTreeprocessor.run and stashedHTML2text._html_sub functions to this README file
- (with a bit of help from this group) wrapped up this assignment for submission

**Alexandru-Valentin Florea**
- added some tests for CodeHilite.__init__ and CodeHiliteExtension.__init__ functions 
- added some parts for CodeHilite.__init__ and CodeHiliteExtension.__init__ functions to this README file

**Robert Sofroni**
- added some tests for dequote and _parseHeader functions
- added some parts for dequote and _parseHeader functions to this README file
