def convert_line(line):
    result=[]
    for val in line.split(":")[1].strip().split(" "):
        if val!="":
            result.append(int(val))
    return result

def calc_old(t, d):

    for i in range(t):
        total_distance = 0
        for j in range(i):
            total_distance+=j
        total_distance+=i*(t-i)
        if total_distance>d:
            return i
def calc_result(t, d):
    total_nums=0
    for i in range(t):
        total_distance=i*(t-i)
        if total_distance>d:
            total_nums+=1
    return total_nums

def main():

    with open("input", "r") as f:
        times=convert_line(f.readline())
        distances =convert_line(f.readline())
        results=[]
        for d,t in zip(distances, times):
            results.append(calc_result(t,d))
        final_val=1
        for res in results:
            final_val*=res
        print(final_val)




if __name__ == "__main__":
    main()

#
