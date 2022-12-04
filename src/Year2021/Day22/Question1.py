class Cube:
    def __init__(self, x1: int, x2: int, y1: int, y2: int, z1: int, z2: int, on: bool):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.on=on

    @staticmethod
    def create(line: str):
        o=line.split(" ")[0]
        return Cube(
            x1=int(line.split("=")[1].split(".")[0]),
            x2=int(line.split("..")[1].split(",")[0]),
            y1=int(line.split("=")[2].split(".")[0]),
            y2=int(line.split("..")[2].split(",")[0]),
            z1=int(line.split("=")[3].split(".")[0]),
            z2=int(line.split("..")[3].split(",")[0]),
            on=o == "on"
        )

    def boom(self, cube):
        if cube.x1 not in range(self.x1, self.x2+1) and cube.x2 not in range(self.x1, self.x2+1):
            return [self]
        if cube.y1 not in range(self.y1, self.y2+1) and cube.y2 not in range(self.y1, self.y2+1):
            return [self]
        if cube.z1 not in range(self.z1, self.z2+1) and cube.z2 not in range(self.z1, self.z2+1):
            return [self]

        xs=cube.x1 <= self.x1 and cube.x2 >=self.x2
        ys=cube.y1 <= self.y1 and cube.y2 >=self.y2
        zs=cube.z1 <= self.z1 and cube.z2 >=self.z2

        if xs and ys and zs:
            return []

        if xs and ys:
            if cube.z1 <= self.z1:
                self.z1 = cube.z2
                return [self]
            if cube.z2 >= self.z2:
                self.z2=cube.z1
                return [self]
            return [Cube(x1=self.x1,
                         x2=self.x2,
                         y1=self.y1,
                         y2=self.y2,
                         z1=self.z1,
                         z2=cube.z1,
                         on=True),
                    Cube(x1=self.x1,
                         x2=self.x2,
                         y1=self.y1,
                         y2=self.y2,
                         z1=cube.z2,
                         z2=self.z2,
                         on=True),
                    ]

        if xs and zs:
            if cube.y1 <= self.y1:
                self.y1 = cube.y2
                return [self]
            if cube.y2 >= self.y2:
                self.y2 = cube.y1
                return [self]

            return [Cube(x1=self.x1,
                         x2=self.x2,
                         y1=self.y1,
                         y2=cube.y1,
                         z1=self.z1,
                         z2=self.z2,
                         on=True),
                    Cube(x1=self.x1,
                         x2=self.x2,
                         y1=cube.y2,
                         y2=self.y2,
                         z1=self.z1,
                         z2=self.z2,
                         on=True),
                    ]

        if ys and zs:
            if cube.x1 <= self.x1:
                self.x1 = cube.x2
                return [self]
            if cube.x2 >= self.x2:
                self.x2 = cube.x1
                return [self]

            return [Cube(x1=cube.x2,
                         x2=self.x2,
                         y1=self.y1,
                         y2=self.y2,
                         z1=self.z1,
                         z2=self.z2,
                         on=True),
                    Cube(x1=self.x1,
                         x2=cube.x1,
                         y1=self.y1,
                         y2=self.y2,
                         z1=self.z1,
                         z2=self.z2,
                         on=True),
                    ]

        if ys:
            pass

        if xs:
            pass

        if zs:
            pass

        else:
            pass #fuck me






def answer(input_file_name):
    with open(input_file_name, "r") as f:
        lines = f.readlines()
    cubes=[]
    for line in lines:
        cubes.append(Cube.create(line))
    on_cubes=[]
    for cube in cubes:
        if cube.on:
            on_cubes.append(cube)
        else:
            n_cubes=[]
            for on_cube in on_cubes:
                n_cube =on_cube.boom(cube)
                n_cubes.extend(n_cube)
            on_cubes=n_cubes



print(answer("input.txt"))
