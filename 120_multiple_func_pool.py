"""
We gonna see how to run multiple functions in a pool


"""

from multiprocessing import Pool

class Functions:
    def f1(self, x):
        return x * x

    def f2(self, x):
        return x + x

    def dispatcher(self, args):
        func_name, value = args
        if func_name == "f1":
            return self.f1(value)
        elif func_name == "f2":
            return self.f2(value)

functions = Functions()
data = [("f1", 1), ("f1", 2), ("f2", 3), ("f2", 4)]

if __name__ == "__main__":
    with Pool() as pool:
        results = pool.map(functions.dispatcher, data)
    print(results)


"""
In the provided code with Pool, each worker in the pool picks up a task, 
which involves calling the dispatcher function. 
Inside dispatcher, based on the func_name, either f1 or f2 is called.

So, if you have 4 cores (for example), and if you've initialized Pool with its default number of processes 
(which usually matches the number of cores), then all 4 tasks in data could potentially run in parallel. 
Each task runs in its own process, but yes, within that process, 
there is a "dispatching" mechanism to decide which function to run.


To break it down:

- One process might handle ("f1", 1) and call f1(1).
- Another process might handle ("f1", 2) and call f1(2).
- A third process might handle ("f2", 3) and call f2(3).
- A fourth process might handle ("f2", 4) and call f2(4).


"""