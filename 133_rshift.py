"""
In Python, the >> operator is typically used for right-shifting bits in an integer or for custom behavior in user-defined classes. 
"""

class ShiftDemo:
    def __init__(self, value):
        self.value = value

    def __rshift__(self, other):
        return self.value >> other

# Usage
shift_demo = ShiftDemo(8)  # Assume 8 is in binary 1000
result = shift_demo >> 2   # This would internally call shift_demo.__rshift__(2)
print(result)  # This would output 2, as 1000 right-shifted by 2 positions is 10 in binary
