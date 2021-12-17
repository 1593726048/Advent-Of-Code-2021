def get_outputs(input_file_name):
    outputs=[]
    with open(input_file_name, "r") as f:
        lines = f.readlines()
    for line in lines:
        outputs.append(line.strip())
    return outputs

my_output=get_outputs("my_test_output")
acutal=get_outputs("test_output")
for val in acutal:
    if val not in my_output:
        print(val)
