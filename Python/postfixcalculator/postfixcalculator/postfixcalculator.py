def calculate(expression):
    # parameters:
    # - expresssion (string) - The arithmetic expression, in postfix notation,
    #   that needs to be evaluated. Each operand and operatior is separated
    #   from one another with a single space. Example:
    #
    #   90 3 12 * +
    #
    # return value:
    # (number) The result when the given arithmetic expression is evaluated.
    #   For the example expresion above, the result should be 126.
    #
    # TODO: Write your code below.

    # Time Complexity: O(n)
    split_expression = expression.split(" ")
    stacked = []
    for i in range(0, len(split_expression)):
        if split_expression[i] == '+' or split_expression[i] == '-' or split_expression[i] == '*' or split_expression[i] == '/':
            a = stacked.pop()
            b = stacked.pop()

            if split_expression[i] == '+':
                stacked.append(int(b) + int(a))
            elif split_expression[i] == '-':
                stacked.append(int(b) - int(a))
            elif split_expression[i] == '*':
                stacked.append(int(b) * int(a))
            elif split_expression[i] == '/':
                stacked.append(int(b) / int(a))
        else:
            stacked.append(split_expression[i])
    return stacked.pop()
    pass