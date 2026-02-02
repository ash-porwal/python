# list and array both are different dataypes
# if we want to store big value then prefer array otherwise prefer list

# to use Array in Python we want to import array
from array import array
from sys import getsizeof

# making array
arr = array('i', range(10_00))
l = list(range(10_00))

print("Array bytes: ", getsizeof(arr))
print("l bytes: ", getsizeof(l))

"""
| Feature             | List                    | Array          |
| ------------------- | ---------------         | -------------- |
| Can store Data Type | Heterogeneous           | Homogeneous    |
| Memory Usage        | Consume more memory     | Lower          |
| Speed (Numeric Ops) | Slower                  | Faster         |
| Built-in            | Yes                     | Module-based   |
| Use Case            | General-purpose         | Numerical data |


List can store heterogeneous data types.
Array Stores homogeneous data only

List Stores references to objects and Uses more memory
Array Stores values in contiguous memory so it is more memory-efficient.

List are faster for general-purpose operations but Slower for heavy numerical computation
Array are faster for numeric and mathematical operations. Optimized for performance (especially NumPy arrays)


List Native Python data structure, so it is rich built-in methods (append, extend, pop)
Array Requires array module or NumPy. Fewer built-in methods (standard array)

Use list when:
    Data types are mixed
    You need flexibility
    General application logic
Use array when:
    Data is numeric
    Memory efficiency matters
    Performance is critical
"""