for i in range(int(input())):   
    try:
        a, b = map(int, input().split())
        print(a//b)  #floor division     
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)