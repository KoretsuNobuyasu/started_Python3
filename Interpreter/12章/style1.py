a = 1
b = 2
print(a)
print(b)
print(c)


"""
nobu-Air:12章 nobuskate$ pylint style1.py
No config file found, using default configuration
************* Module style1
C:  5, 0: Final newline missing (missing-final-newline)
C:  1, 0: Missing module docstring (missing-docstring)
C:  1, 0: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
C:  2, 0: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
E:  5, 6: Undefined variable 'c' (undefined-variable)

------------------------------------
Your code has been rated at -8.00/10
"""