def precedence(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for ch in expression:
        if ch.isalnum():
            postfix += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(ch)):
                postfix += stack.pop()

            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix


def evaluate_postfix(postfix):
    stack = []

    for ch in postfix:
        if ch.isdigit():
            stack.append(float(ch))

        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)
            elif ch == '^':
                stack.append(a ** b)

    return stack.pop()


# Main Program
expression = input("Enter infix expression: ")

postfix = infix_to_postfix(expression)

print("Postfix Expression:", postfix)

if any(ch.isalpha() for ch in expression):
    print("Evaluation skipped (expression contains variables, not digits).")
else:
    result = evaluate_postfix(postfix)
    print("Evaluation Result:", result)
