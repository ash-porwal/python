# Basic structured
# {key_expression: value_expression for item in iterable}

numbers = [1, 2, 3, 4]
squares = {number: number**2 for number in numbers}
print(squares)


# Conditional Dictionary Comprehension
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {number: number**2 for number in numbers if number % 2 == 0}
print(even_squares)


# a bit complex
students_scores = [("Alice", [88, 92, 80]), ("Bob", [85, 90, 88]), ("Charlie", [80, 95, 78])]

students_stats = {
    student: {
        "average": sum(scores) / len(scores),
        "max": max(scores),
        "min": min(scores)
    } for student, scores in students_scores
}
# students_stats = { k:sum(v)/len(v) for k, v in students_scores}
print(students_stats)