from ai_pkg.search import *

start = 'kota_B'
goal = 'kota_G'

city_map = Graph(dict(
    kota_A=dict(kotaB=1500,kota_C=500,kota_D=1000),
    kota_B=dict(kota_E=500,kota_F=500),
    kota_C=dict(kota_T=400,kota_H=600),
    kota_D=dict(kota_T=500,kota_I=500),
    kota_F=dict(kota_T=600,kota_G=400),
    kota_H=dict(kota_T=400)
    ), directed=True)


class CityProblem(Problem):
    def __init__(self, initial, goal, graph):
        Problem.__init__(self, initial, goal)
        self.graph = graph

    def actions(self, A):
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        return action

    def path_cost(self, cost, A, action, B):
        return cost + (self.graph.get(A, B) or infinity)


def breadth_first_search(problem):
    global track_path
    frontier = deque([Node(problem.initial)])
    explored = set()
    track_path = [problem.initial]
    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        expanded = node.expand(problem)
        for child in expanded:
            track_path.append(child.state)
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None

if __name__ == '__main__':
    track_path = []
    romania_problem = CityProblem(start, goal, city_map)
    node = breadth_first_search(romania_problem)

    if node is not None:
        final_path = node.solution()
        final_path.insert(0, start)
        print('TRACKING PATH: ', ' -> '.join(track_path))
        print('SOLUTION PATH: ', ' -> '.join(final_path))
