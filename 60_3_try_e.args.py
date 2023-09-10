try:
    raise ValueError("Some error message", "Additional info")
except Exception as e:
    print("Using str(e):", str(e))
    print("Using e.args:", e.args) #e.args is a tuple containing the arguments that were passed to the exception
    print("Using e.args[0]:", e.args[0])
