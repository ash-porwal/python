# Slicing is used to access parts of sequences like lists, tuples, and strings.
# String Slicing:
# A string in Python can be sliced for getting a part of the string. ..like if we want just two character from ashish
# The index in a string starts from 0 to (length-1) in Python.
name = 'Ashish'
print(name[0])
print(name[4]) # we can get any character of that particular index if we put that index number
# if we want to change a particular index like
# name [3] = 'f' #this wont work... so we cannot change any  
print(name[0:3]) # ye bol raha hai ki print karo name variables 0 se 2 tak ke index ..i.e. 0,1,2 indexes will be print (3rd index wont print)..and this is called string slicing
#print(name[:4])..here it will take from min to 3
#print(name[2:])..here it will take from 2 to last index

# Python general syntax for slicing: sequence[start:stop:step]


#negative index ...in negative counting last character of string will be -1, then second last will be -2 and so on
print(name[-4 : -1])
print(name[-4 : ])
# print(name[-1 : -4]) # this wont work because counting should start from lower number first then higher number

#skipping of string
d = "qwertyuioplkjhgfdsa"
print(d[0:4:1]) # ye last wali jo value hai iska kaam hai jaise we have 1 at the end to iska matalb hai koi character skip na karo...agar uski jagah 2 hota to ek character skip hoke aata
print(d[0:8:2])
print(d[1:8:2])
print(d[0::2])
print(d[0::3])
print(d[1:9:3])

'''
we read this name[0:4] as - 
----name from index 0 to 3-----
'''

### NEGATIVE SLICING
'''
- In general syntax of python -> [start: stop: step]
  If "step" is negative, the slicing starts from "start" and moves backward towards(to the left) "stop".

  Example:
    s = [0, 1, 2, 3, 4, 5]
    print(s[1:4:-1])  # Output: []

  👉 Why does this return an empty list ([])?
    start = 1 → This refers to s[1] (1).
    stop = 4 → This refers to s[4] (4).
    step = -1 → Moves backward.

  💡 Problem:
      The slicing starts at index 1 (1).
      But step = -1 expects movement backward.
      However, stop (4) is ahead of start (1), making it impossible to move backward.
      👉 Result? Python returns an empty list ([]) because the range makes no sense.



    So, if we have slicing like this
      s = [0, 1, 2, 3, 4, 5]
      print(s[4:1:-1])  # Output: [4, 3, 2]


    In, case if we dont provide "start" and "stop" then it reverse it.
    s = "Python"
    print(s[::-1])  # Output: "nohtyP"

--------

- When using negative values in slicing, you are defining the start and end points 
  of the slice relative to the end of the string.
    - name[-1] retrieves the last character of the string.

    - name[-4:] retrieves the last four characters of the string.

    - name[:-2] captures everything from the start to just before the second-last character

    - name[-3:-1] retrieves the substring starting from the third-last character to 
                  just before the last character (i.e., the third-last and 
                  second-last characters).

- We know slicing has 3 things - start, end and step
  Negative steps are used to reverse the direction of the slice.
  - name[::-1] reverses the entire string.
  - name[5:1:-1] starts from index 5 and moves backwards to just after index 1 (thus, index 2).

  - "Ashish"[-1:-4:-1] will start from the last character and move backwards, stopping just before the character at index -4 (which corresponds to m). This slice would give you "hsi".

Q: Why does this slicing return an empty list?
    s = [100, 200, 300, 400, 500]
    print(s[4:0])
Answer: this returns empty list because, it starts with index 4 and stops at index 0, 
        and as "step" is not mentioned, so it takes "+1" as a default value, 
        so it does not go for backward slicing, so it returns empty list []
'''
