
def read():


    #with open("example.txt", "r") as file: data = file.readline()
    #print(f"hey {data}") 
  try:
    with open("example.txt","r+") as dile: 
       dile.write("hello tr froe pythoner")
       dile.seek(0)
       output = dile.read()
       print(f"hey {output}") 
  except Exception as e:
    print(f" The erro is {e} ")
  finally:
    print("\n Hadi mmi nimehanmg, oh nimeelewa")

read()