from queue import PriorityQueue
import math
"""
定义了一个用来创建地图的类
其中包含了障碍物的设置、邻居的获取、移动代价的计算(因为这里我默认的是网格地图,所以两相邻节点的移动代价为1)等方法
"""
class GridMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # 障碍物的集合
        self.walls = set()

    # 判断某点是否在地图内
    def in_bounds(self, node):
        x, y = node
        return 0 <= x < self.width and 0 <= y < self.height

    # 判断某点是否可通行
    def passable(self, node):
        return node not in self.walls

    # 获取某个节点的邻居节点
    def neighbors(self, node):
        x, y = node
        #上下左右四个方向的邻居节点
        results = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        # 过滤不在地图内的节点
        results = filter(self.in_bounds, results)

        # 过滤障碍物
        results = filter(self.passable, results)

        return results

    # 移动的代价
    def cost(self, current, next):
        return 1

#启发式算法的预估代价，使用的是曼哈顿距离

def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


"""
A*算法的实现
实现过程：
1.初始化一个优先队列作为开放列表，存储待探索的节点
2.初始化一个字典来记录每个节点的父节点，用于更新最短路径和回溯路径
3.初始化一个字典来记录从起点到某个节点的实际代价
4.将起点加入开放列表，设置其实际代价为0
5. 开始搜索
6.从优先队列中取出代价最低的节点作为当前节点
7.如果当前节点是终点，搜索结束
8.遍历当前节点的邻居节点，计算从起点到邻居节点的实际代价
9.如果邻居节点未被访问过或者通过当前节点到邻居节点的代价更低，更新邻居节点的实际代价和父节点，计算邻居节点的总代价并将邻居节点加入优先队列
10.重复步骤6-9，直到找到终点或者优先队列为空停止

重要变量说明：
frontier:优先队列，存储待探索的节点，按照总代价排序
came_from:字典，记录每个节点的父节点，用于更新最短路径和回溯路径
cost_so_far:字典，记录从起点到某个节点的实际代价
priority:变量，邻居节点的总代价（实际代价 + 预估代价），用于在优先队列中排序
"""
def a_star_search(graph, start, goal):

    frontier = PriorityQueue()

    # (排序的优先级, 节点)
    frontier.put((0, start))

    came_from = dict()
    cost_so_far = dict()

    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():

        _, current = frontier.get()

        # 找到终点
        if current == goal:
            break

        # 遍历邻居
        for next in graph.neighbors(current):

            new_cost = cost_so_far[current] + graph.cost(current, next)

            # 更新更短路径
            if next not in cost_so_far or new_cost < cost_so_far[next]:

                cost_so_far[next] = new_cost

                # 总代价 = 已经走过的代价 + 预估剩余代价
                priority = new_cost + heuristic(goal, next)

                frontier.put((priority, next))

                came_from[next] = current

    return came_from, cost_so_far
#路径回溯函数，从终点开始通过父节点回溯到起点，构建出完整的路径
def reconstruct_path(came_from, start, goal):

    current = goal

    path = []

    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)

    path.reverse()

    return path
#主函数
if __name__ == "__main__":

    #创建地图
    graph = GridMap(10, 10)

    #设置障碍物
    graph.walls = {
        (3, 3),
        (3, 4),
        (3, 5),
        (4, 5),
        (5, 5),
        (6, 5)
    }
    #设置起点和终点
    start = (0, 0)
    goal = (8, 8)

    # A*搜索
    came_from, cost_so_far = a_star_search(graph, start, goal)

    # 回溯路径
    path = reconstruct_path(came_from, start, goal)

    print("路径：")
    print(path)
    #可视化地图和路径
    for y in range(graph.height):

        for x in range(graph.width):

            point = (x, y)

            if point == start:
                print("S", end=" ")

            elif point == goal:
                print("G", end=" ")

            elif point in graph.walls:
                print("#", end=" ")

            elif point in path:
                print("*", end=" ")

            else:
                print(".", end=" ")

        print()