import time
samaye = int(input("Enter the count down in seconds: "))


while 0 < samaye:
    time.sleep(1)
    print(f"tick tick- {samaye}")
    samaye-=1
# else: 
    # print('Please enter a positive interger')
print("Over!!!")



# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60) #The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).  divmod(dividend, divisor)
#         # so mins variable will get quotient value and secs will get remainder value
#         timer = "Timer- {:02d}:{:02d}".format(mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1
    
#     print("Time Over!!!")

# t = input("Enter time(seconds): ")

# countdown(int(t))