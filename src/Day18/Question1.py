from ast import literal_eval


class Pair:
    def __init__(self, left, right, parent=None):
        if isinstance(left, Pair):
            left.parent = self
            self.left = left
        elif isinstance(left, list):
            self.left = Pair(left[0], left[1], self)
        else:
            self.left = left

        if isinstance(right, Pair):
            right.parent = self
            self.right = right
        elif isinstance(right, list):
            self.right = Pair(right[0], right[1], self)
        else:
            self.right = right
        self.parent = parent

    def explode(self):
        left_val = None
        cur_node = self
        while left_val is None and cur_node.parent is not None:
            parent = cur_node.parent
            if parent.left is not cur_node:
                left_val = parent
            cur_node = parent

        right_val = None
        cur_node = self
        while right_val is None and cur_node.parent is not None:
            parent = cur_node.parent
            if parent.right is not cur_node:
                right_val = parent
            cur_node = parent

        while isinstance(left_val, Pair) and isinstance(left_val.right, Pair):
            left_val = left_val.right
            print(left_val.get_list())

        while isinstance(right_val, Pair) and isinstance(right_val.left, Pair):
            right_val = right_val.left
            print(right_val.get_list())

        if left_val is not None:
            print(f"l: {left_val.get_list()}")

        if right_val is not None:
            print(f"r: {right_val.get_list()}")

        if right_val is not None:
            right_val.left += self.right
        if left_val is not None:
            left_val.right += self.left

        if left_val is not None:
            print(f"l: {left_val.get_list()}")
        if right_val is not None:
            print(f"r: {right_val.get_list()}")
        print()

        if self.parent.right is self:
            self.parent.right = 0
        else:
            self.parent.left = 0

    def check_explode(self, num):
        if num >= 4:
            if isinstance(self.left, int) and isinstance(self.right, int):
                self.explode()
                return True

        if isinstance(self.left, Pair):
            if self.left.check_explode(num + 1):
                return True
        else:
            if self.left >= 10:
                self.left = Pair(self.left // 10, self.left % 10, self)
                return True

        if isinstance(self.right, Pair):
            if self.right.check_explode(num + 1):
                return True
        else:
            if self.right >= 10:
                self.right = Pair(self.right // 10, self.right % 10, self)
                return True
        return False

    def add(self):
        val = 0
        if isinstance(self.left, int):
            val += self.left
        else:
            val += self.left.add()
        if isinstance(self.right, int):
            val += self.right
        else:
            val += self.right.add()
        return val

    def get_list(self):
        lis = []
        if isinstance(self.left, int):
            lis.append(self.left)
        else:
            lis.append(self.left.get_list())

        if isinstance(self.right, int):
            lis.append(self.right)
        else:
            lis.append(self.right.get_list())
        return lis


def answer(input_file_name):
    with open(input_file_name, "r") as f:
        lines = f.readlines()
    left_tree = None
    for line in lines:
        arr = literal_eval(line.strip())
        tree = Pair(arr[0], arr[1])
        if left_tree is None:
            left_tree = tree
        else:
            left_tree = Pair(left_tree, tree)

    print(left_tree.get_list())
    while left_tree.check_explode(0):
        print(left_tree.get_list())
    return left_tree.add()


# print(answer("example.txt"))
print(answer("Example2"))
# print(answer("input.txt"))
# 4027
