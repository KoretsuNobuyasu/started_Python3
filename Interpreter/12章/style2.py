a = 1
b = 2
c = 3
print(a)
print(b)
print(c)


"""
nobu-Air:12章 nobuskate$ pylint style2.py
No config file found, using default configuration
************* Module style2
C:  6, 0: Final newline missing (missing-final-newline)
C:  1, 0: Missing module docstring (missing-docstring)
C:  1, 0: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
C:  2, 0: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
C:  3, 0: Constant name "c" doesn't conform to UPPER_CASE naming style (invalid-name)

-----------------------------------
Your code has been rated at 1.67/10
"""