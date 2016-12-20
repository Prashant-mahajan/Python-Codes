n = int(input())

#takes input in sapce separated form & creates list of name & number
name_number = [input().split() for _ in range(n)]

#represent list in the form of dictionary with name:number pair
phoneBook = {name : number for name, number in name_number} 

while(True):
    try: 
    #this will continue to run till the EOF
        name = input()
        if name in phoneBook:
            print("%s=%s " %(name,phoneBook[name]))
        else:
            print("Not found")
    except:
        break