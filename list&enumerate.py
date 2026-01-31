items=[1,2,3,4,5,6,7]
for index,value in enumerate(items):
      print(index,value)
      if value==5:
          break
print("*************")
for i in range(len(items)):
    print(i,items[i])
    if items[i]==4:
        break
