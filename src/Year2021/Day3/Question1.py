def answer(input_file_name):
    total=0
    nums=[0]*12
    with open(input_file_name, "r") as f:
        line = f.readline()
        i = 0
        while line != "":
            for i in range(12):
                nums[i]+=int(line[i])
            total+=1
            line = f.readline()
        half=total/2
        gamma_binary=[0]*12
        epsilon_binary = [1] * 12
        gamma_b_str=""
        epsilon_b_str = ""
        for i in range(12):
            if nums[i]>half:
                gamma_binary[i]=1
                epsilon_binary[i]=0

            gamma_b_str+=str(gamma_binary[i])
            epsilon_b_str += str(epsilon_binary[i])
        gamma=int(gamma_b_str, 2)
        epsilon=int(epsilon_b_str,2)
        print(gamma)
        print(epsilon)
        print(epsilon*gamma)
answer("input.txt")