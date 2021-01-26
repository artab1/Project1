Shopping_lists = [
                    ["Apple","Mango","Orange"],
                    ["Banana","Orange","Mango","Water melon"],
                    ["Grapes","Apple","Banana","Chilli","Water melon"],
                    ["Chilli","Mango","Banana","Chilli","Grapes","Apple","Banana","Chilli","Water melon"],
                    ["Apple","Mango","Apple","Grapes","Apple","Banana","Apple","Chilli","Water melon"],
                    ["Apple","Orange","Banana","Mango","Grapes","Apple","Banana","Chilli","Water melon"],
]


for fruit in Shopping_lists:
    for value in range(len(fruit) -1, -1, -1):
        if (fruit[value]) == "Chilli":
            del fruit[value]
        
    print(", ".join(fruit))
    
#for ind_list in Shopping_lists:
 #   for fruit in ind_list:
  #      if fruit != "Chilli":
   #         print(fruit)

    #print()