def ls(lines, i):
    file_list = {}
    while i < len(lines) and lines[i][0] != "$":
        if lines[i].split(" ")[0] == "dir":
            pass
        else:
            file_list[lines[i].split(" ")[1].strip()] = int(lines[i].split(" ")[0])
        i += 1
    return file_list, i


def count_folder_size(folder_dict):
    total = 0
    for key in folder_dict:
        if isinstance(folder_dict[key], dict):
            total += count_folder_size(folder_dict[key])
        else:
            total += folder_dict[key]
    return total


def count_at_most(folder_dict, max_size):
    total = count_folder_size(folder_dict)
    if total > max_size:
        total = 0
    for key in folder_dict:
        if isinstance(folder_dict[key], dict):
            total += count_at_most(folder_dict[key], max_size)

    return total


def print_out(folder_dict, num_indents=0):
    for key in folder_dict:
        if isinstance(folder_dict[key], dict):
            print("   " * num_indents, end="")
            print(key)
            print_out(folder_dict[key], num_indents + 1)
        else:
            print("   " * num_indents, end="")
            print(key)


def main():
    folder_dict = {}
    current_folder = folder_dict
    current_path = []
    with open("input", "r") as f:
        i = 1
        lines = f.readlines()
        while i < len(lines):
            if lines[i][0] == "$":
                if lines[i][2:4] == "ls":
                    i += 1
                    temp, i = ls(lines, i)
                    current_folder.update(temp)
                    i -= 1
                elif lines[i][2:4] == "cd":
                    if lines[i][5:] == "..\n":
                        temp_path = []
                        current_folder = folder_dict
                        for path_slice in current_path[:-1]:
                            temp_path.append(path_slice)
                            current_folder = current_folder[path_slice]
                        current_path=temp_path
                    else:
                        current_path.append(lines[i][5:].strip())
                        temp = {}
                        current_folder[lines[i][5:].strip()] = temp
                        current_folder = temp
                else:
                    pass
            i += 1
    print(count_at_most(folder_dict, 100000))


if __name__ == "__main__":
    main()

# 3790902
