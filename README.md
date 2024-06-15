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

The coverage check is done with [coverage.py](https://github.com/nedbat/coveragepy). The following command is used to check the total coverage throughtout the project:
```
$ coverage run -m unittest discover
```

Total function coverage was 95%:</p>
<img src="https://i.ibb.co/y6VkxkY/image.png" width="600"></p>

### Your own coverage tool

<The following is supposed to be repeated for each group member>

**Said Musab Oguz**

- Function name: parse_hl_lines

[Link to the patch (diff)](https://github.com/Dolyetyus/markdown/commit/d07b27274c416ae258ec3d1003a9b26a51fed749?diff=unified&w=1)

Screenshot of the coverage results:</p>
<img src="https://i.ibb.co/DCRzTGC/image.png" width="600"></p>

<Provide a screenshot of the coverage results output by the instrumentation>

- Function name: hilite

[Link to the patch (diff)](https://github.com/Dolyetyus/markdown/commit/d07b27274c416ae258ec3d1003a9b26a51fed749?diff=unified&w=1)

Screenshot of the coverage results:</p>
<img src="https://i.ibb.co/HGK6X27/image.png" width="600"></p>

**Mihnea Bârsan**

- Function name: 

[Link to the patch (diff)]()

Screenshot of the coverage results:</p>

<Provide a screenshot of the coverage results output by the instrumentation>

- Function name:

[Link to the patch (diff)]()

Screenshot of the coverage results:</p>

**Robert Sofroni**

- Function name: 

[Link to the patch (diff)]()

Screenshot of the coverage results:</p>

<Provide a screenshot of the coverage results output by the instrumentation>

- Function name:

[Link to the patch (diff)]()

Screenshot of the coverage results:</p>

**Alexandru Florea**

- Function name: 

[Link to the patch (diff)]()

Screenshot of the coverage results:</p>

<Provide a screenshot of the coverage results output by the instrumentation>

- Function name:

[Link to the patch (diff)]()

Screenshot of the coverage results:</p>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

**Said Musab Oguz**

#### Test: codehilite

[Link to the patch (diff) for the new test file](https://github.com/Dolyetyus/markdown/commit/f8a67f6aab90ee436302e72e8ccdba6cd3e79ba1?diff=unified&w=1)

**Old coverage result:** </p>
<img src="https://i.ibb.co/HGK6X27/image.png" width="600"></p>

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
<img src="https://i.ibb.co/DCRzTGC/image.png" width="600"></p>

**New coverage result:** </p>
<img src="https://github.com/Dolyetyus/markdown/assets/67073431/a8b3c9aa-b8b1-4f12-a3c8-f591d1aaafe2" width="600"></p>

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

**Alexandru Florea**

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>
