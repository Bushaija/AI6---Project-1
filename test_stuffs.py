# using assert

"""
    assert is used to set conditions that must be true during execution.
    it helps in debugging, by raising `AssertionError` if condition is False.
"""

def divide(a,b):
    assert b != 0
    return a/b

#print(divide(2,1))

# strip().split() chain
name = "riwa chapters"
print(name.strip().strip())
