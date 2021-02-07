# git, github & CI basics

1. Clone this repository
2. Come up with a reasonable real-world requirement for a list or a function on one or more lists
3. Create an issue labelled "Test for ... is missing"
4. Add a corresponding unit test
5. Add your name to the CONTRIBUTORS file
6. Push the code to a new branch
7. Create a pull requests saying "Closes #..." (referencing your issue)
8. Make sure your tests are green and your PR is mergeable

## Examples of functions:
- test that empty list `e` + any list `l` is equal to `l`
- test that list `l` with an element `e` filtered out does not contain `l`
- test that `sum(l)` is equal to a sum of `l`'s elements
- test that list concatenation works as expected
- ...

Note: we don't practice writing proper unit tests here in the sense that you are allowed to write _any_ code that involves lists as long as it's sensible.

In a real world, one of requirements for unit tests is that they should cover only code that is directly under scrutiny, i.e. if we test lists, we test their construction, concatenation, element addition, removal, lookup etc. When we are asserting e.g.

`list(map(lambda x: x + 1, [1,2,3])) == [2,3,4]`,

we are actually testing the `map` function. 

However, for our purposes this is fine as long as you remember this argument.
