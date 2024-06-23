# Report for Assignment 1

## Project chosen

Name: Python-Markdown

URL: https://github.com/Python-Markdown/markdown

Number of lines of code and the tool used to count it: Total number of lines of code: 17295. </br></br>
Tested by using Lizard to count the nloc.</br>
<img src="https://i.ibb.co/Pr4ZjNc/Whats-App-Image-2024-06-07-at-01-41-00-31a65e5a.jpg" width="600"></p>

Programming language: Python 3

## Coverage measurement

### Existing tool

The coverage check is done with [coverage.py](https://github.com/nedbat/coveragepy). The following command is used to check the total coverage throughout the project:
```
$ coverage run -m unittest discover
```

Total function coverage was 95%:</p>
<img src="https://github.com/Dolyetyus/markdown/assets/67073431/d40bb79d-5aa0-4910-9840-a81a2ccd36f7" width="600"></p>

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

- Function name: HiliteTreeprocessor.run 

[Link to the patch (diff)](https://github.com/Dolyetyus/markdown/commit/701416ad42d5470a5cb28fe74d31e16a9e329537?diff=unified&w=0)

Screenshot of the coverage results:</p>

<Provide a screenshot of the coverage results output by the instrumentation>

- Function name:

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

Screenshot of the coverage results:</p>

**Robert Sofroni**

- Function name: 

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

Screenshot of the coverage results:</p>

<Provide a screenshot of the coverage results output by the instrumentation>

- Function name:

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

Screenshot of the coverage results:</p>

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

#### Test: codehilite

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

**Mihnea Bârsan**

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

**Robert Sofroni**

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

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

**Results of the old coverage results by running the existing tool (coverage.py):** </p>
<img src="https://github.com/Dolyetyus/markdown/assets/67073431/d40bb79d-5aa0-4910-9840-a81a2ccd36f7" width="600"></p>

**Results of the new coverage results by running the existing tool using all test modifications made by the group:** </p>
*We will run the tool again after all of us are done and we merge our tests*

## Statement of individual contributions

*Write here what each group member did*
