import unittest

"""
First attempt uses loops to iterate through the
list of floats passed in, calculates the powerof
for each element appeneding to a new list, and
returns the sum of the new list
"""
def function_example1(inputlist, powerto, scale):
    result = []
    if scale == True:
        for i in inputlist:
            result.append(i**powerto)
    else:
        for i in inputlist:
            result.append(i**(powerto*2))

    return sum(result)

"""
Add annotations to arguments to make it clearer what the function accepts
"""
def function_example2(inputlist:'list[float]', powerto:'int', scale:'bool')->'float':
    result = []
    if scale == True:
        for i in inputlist:
            result.append(i**powerto)
    else:
        for i in inputlist:
            result.append(i**(powerto*2))

    return sum(result)

"""
Use a list comprehension instead of the looping approach
"""
def function_example3(inputlist:'list[float]', powerto:'int', scale:'bool')->'float':
    result = []
    if scale == True:
        result = [i**powerto for i in inputlist]
    else:
        result = [i**(powerto*2) for i in inputlist]

    return sum(result)

"""
Use a generator expression, with large data sets should use less memory
"""
def function_example4(inputlist:'list[float]', powerto:'int', scale:'bool')->'float':
    result = 0
    if scale == True:
        result = sum(i**powerto for i in inputlist)
    else:
        result = sum(i**(powerto*2) for i in inputlist)

    return result

class TestFunctionExamples(unittest.TestCase):
    def test_function_example1_scale_true_success(self):
        input = [0.5, 0.6, 0.1]

        res = function_example1(input, 2, True)
        expected = 9
        self.assertEqual(res, expected)

    def test_function_example1_scale_false_success(self):
        input = [0.5, 0.6, 0.1]

        res = function_example1(input, 2, True)
        expected = 9
        self.assertEqual(res, expected)

    def test_function_example2_scale_true_success(self):
        input = [0.5, 0.6, 0.1]

        res = function_example2(input, 2, True)
        expected = 9
        self.assertEqual(res, expected)

    def test_function_example2_scale_false_success(self):
        input = [0.5, 0.6, 0.1]

        res = function_example2(input, 2, True)
        expected = 9
        self.assertEqual(res, expected)

    def test_function_example3_scale_true_success(self):
        input = [0.5, 0.6, 0.1]

        res = function_example3(input, 2, True)
        expected = 9
        self.assertEqual(res, expected)

    def test_function_example3_scale_false_success(self):
        input = [0.5, 0.6, 0.1]

        res = function_example3(input, 2, True)
        expected = 9
        self.assertEqual(res, expected)

    def test_function_example4_scale_true_success(self):
        input = [0.5, 0.6, 0.1]

        res = function_example4(input, 2, True)
        expected = 9
        self.assertEqual(res, expected)

    def test_function_example4_scale_false_success(self):
        input = [0.5, 0.6, 0.1]

        res = function_example4(input, 2, True)
        expected = 9
        self.assertEqual(res, expected)