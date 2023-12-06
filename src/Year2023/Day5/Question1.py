class SourceDest:
    class Slice:
        def __init__(self, source, destination, increment):
            self.source = source
            self.destination = destination
            self.increment = increment

        def get_value(self, source):
            if source in range(self.source, self.source+self.increment):
                return self.destination+source-self.source

        def __repr__(self):
            return f"{self.source} {self.destination} {self.increment}"

    def __init__(self, source, dest):
        self.dest = dest
        self.source = source
        self.slices = []

    def add_numbers(self, line):
        destination,source, increment = [int(i) for i in line.split(" ")]
        self.slices.append(SourceDest.Slice(source, destination, increment))

    def get_value(self, source):
        for val in self.slices:
            num = val.get_value(source)
            if num is not None:
                return num
        return source
    def __repr__(self):
        return f"{self.source} to {self.dest}: {self.slices}"


def func2():
    pass


def main():
    sds=[]
    sd=None
    with open("input", "r") as f:
        seeds= [int(i) for i in f.readline().split(": ")[1].split(" ")]
        for line in f.readlines():
            if line =="\n":
                pass
            elif ":" in line:
                if sd is not None:
                    sds.append(sd)
                sd=SourceDest(line.split("-to-")[0],line.split("-to-")[1].split(" ")[0])
            else:
                sd.add_numbers(line)
    sds.append(sd)
    print(seeds)
    print(sds)
    previous_seeds=seeds
    for sd in sds:
        new_seeds=[]
        for seed in previous_seeds:
            new_seeds.append(sd.get_value(seed))
        previous_seeds=new_seeds
        print(previous_seeds)
    print(previous_seeds)
    print(min(previous_seeds))


if __name__ == "__main__":
    main()

#
