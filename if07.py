def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    x = abs(a)
    if 10 <= x <= 99:
        if x % 2 == 0:
            return "ikki xonali juft son"
        return "ikki xonali toq son"
    if 100 <= x <= 999:
        if x % 2 == 0:
            return "uch xonali juft son"
        return "uch xonali toq son"
    return "boshqa son"

print(main(-242))
print(main(57))