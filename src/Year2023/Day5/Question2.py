from typing import List


class Source:
    def __init__(self, start, increment):
        self.increment = increment
        self.start = start
        self.end=start+increment

    @staticmethod
    def other_init(start, end):
        return Source(start, end-start)

    def __repr__(self):
        return f"{self.start}-{self.end}"

class SourceDest:
    class Slice:
        def __init__(self, source, destination, increment):
            self.source = source
            self.destination = destination
            self.increment = increment

        def process_source(self, val):
            return self.destination+val-self.source

        def get_value(self, sources: List[Source]):
            unprocessed_sources=[]
            processed_sources=[]
            for source in sources:
                if source.end<self.source or source.start>self.source+self.increment:
                    unprocessed_sources.append(source)
                elif self.source<=source.start and source.end >= self.source+self.increment:
                    processed_sources.append(Source(self.process_source(source.start), source.increment))
                elif self.source<=source.start:
                    processed_sources.append(Source.other_init(
                        self.process_source(self.source),
                        self.process_source(source.end))
                    )
                    unprocessed_sources.append(Source.other_init(source.start, self.source-1))
                elif source.end >= self.source+self.increment:
                    processed_sources.append(Source.other_init(
                        self.process_source(self.source),
                        self.process_source(self.source + self.increment))
                    )
                    unprocessed_sources.append(Source.other_init(self.source + self.increment + 1, source.end))
                else:
                    processed_sources.append(Source.other_init(
                        self.process_source(self.source),
                        self.process_source(self.source+self.increment)
                    )
                    )
                    unprocessed_sources.append(Source.other_init(source.start, self.source))
                    unprocessed_sources.append(Source.other_init(self.source+self.increment+1,source.end))
            return processed_sources,  unprocessed_sources

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
        processed_sources=[]
        unprocessed_sources=[]
        print(source)
        unprocessed_sources.extend(source)
        for val in self.slices:
            pro, unpro = val.get_value(unprocessed_sources)
            processed_sources.extend(processed_sources)
            unprocessed_sources.extend(unpro)
        processed_sources.extend(unprocessed_sources)
        return processed_sources
    def __repr__(self):
        return f"{self.source} to {self.dest}: {self.slices}"


def func2():
    pass


def main():
    sds=[]
    sd=None
    with open("test", "r") as f:
        old_seeds= [int(i) for i in f.readline().split(": ")[1].split(" ")]
        sources=[]
        for i in range(len(old_seeds)//2):
            sources.append(Source(old_seeds[i*2],old_seeds[i*2+1]))
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
    previous_seeds=sources
    for sd in sds:
        previous_seeds=sd.get_value(previous_seeds)
    print("\n\n\n")
    print(previous_seeds)
    #print(min(previous_seeds))


if __name__ == "__main__":
    main()

#
