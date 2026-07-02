from auto_docsting_readme.main import auto_docstr_readme

@auto_docstr_readme
def addition(a, b):
    """The function adds a and b together"""
    return a + b

@auto_docstr_readme(language="zh")
def squad(a, b):
    """The function raises a to the power of b"""
    return a ** b

if __name__ == "__main__":
    addition(2, 2)
    squad(2, 6)