def Writer():
    try:
        with open("input.txt","w") as MyFile:
            for x in range(5):
               word = input(f"\n Enter {x+1} text \n")
               MyFile.write(word + "\n")
    except Exception as e:
       print(f"The error is{e}")

def reader():
    try:
        with open("input.txt", "r") as MyFile:
            Words = MyFile.read() 
                     
        print(f"{Words}")

#The Words Count is below:
        count = 0
        for x in Words:         
            count +=1
        print(f"\nthe Count is {count}")
#The Caps words is below:
        with open("output.txt","w") as MyFile:
             c = Words.upper()
             MyFile.write(c)
            

    except Exception as e:
        print(f"The error is{e}")

    finally:
        print("\n The Program runs Okay!!")

reader()