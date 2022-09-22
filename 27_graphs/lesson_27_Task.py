# task 1
class Graph:
    def __init__(self, graph: dict = None):
        if graph is None:
            graph = {}
        self.graph = graph

    def dfs(self):
        for vertex in self:
            if vertex.color == "white":
                self.dfs_visit(vertex)

# task 2
...


# start
def main():
    # task 1
    ...
    # task 2
    ...


if __name__ == "__main__":
    main()