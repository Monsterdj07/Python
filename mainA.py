for i in range(2,21):
     with open(f"{i}.text","w") as f:
        for j in range(1,11):
            f.write(f"{i} * {j} = {i*j} \n")