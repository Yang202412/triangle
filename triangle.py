star= int(input("請輸入幾層空心正三角形: "))
curr_num = 0
if star<=1:
    exit()
for i in range(star):
    for j in range(star):
        if (i== star- j) or ((i == star - 1) and (j%2 != 0)):
            print("*", end="")
        else:
            print(" ", end="")
    for k in range(star):
        if (i == k) or ((i == star - 1) and (k%2 == 0) and (k != star -2)):
            print("*", end="")
        else:
            print(" ", end="")
    print("")
    
            