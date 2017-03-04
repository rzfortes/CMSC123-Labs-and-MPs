import unittest

from postfixcalculator import calculate


testcases = {
    '2 3 +': 5,
    '90 3 -': 87,
    '10 4 3 + 2 * -': -4,
    '10 4 3 + 2 * - 2 /': -2,
    '90 34 12 33 55 66 + * - + -': 4037,
    '1 2 + 4 *': 12,
    '5 1 2 + 4 * + 3 -': 14,
    '1 1 + 1 +': 3,
    '2 3 * 4 *': 24,
    '5 1 2 + 4 * + 3 -': 14,
    '4 4 + 2 *': 16,
    '5 5 * 5 + 10 - 4 /': 5,
    '-1 2 -': -3,
    '2 3 11 + 5 - *': 18,
    '3 11 + 5 -': 9,
    '3 11 5 + -': -13,
    '2 1 12 3 / - +': -1,
    '3 2 * 11 -': -5,
}


class PostfixCalculatorTestCase(unittest.TestCase):

    def test_should_evaluate_postfix_expression(self):
        for expression, result in testcases.items():
            try:
                self.assertEqual(calculate(expression), result)
            except AssertionError as e:
                error = '\'{}\' should be {}'.format(expression, result)
                self.fail(error)


if __name__ == '__main__':
    unittest.main()
