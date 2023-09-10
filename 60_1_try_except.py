while True:    
    try:
        n1 = int(input("Enter num1: ").lower())
        n2 = int(input("Enter num2: ").lower())
        print(n1+n2)
    
   

    except Exception as e:
        print("You Stupid!")
        print(e)
    # print("Done!")

    if n1 == 'q' or n2 == 'q':
        break