origin = input("Origem: ").strip().title()
destiny = input("Destino: ").strip().title()
if origin == "Bh":
    origin = "Belo Horizonte"
elif destiny == "Bh":
    destiny = "Belo Horizonte"


class Graph_MG:
    def __init__(self, lines, points):
        self.l = lines
        self.p = points
        self.size = len(points)

    def adjacent(self, x):
        return self.l[x]


def min_heapify(list, index):
    n = len(list)
    left, right, small = 2 * i + 1, 2 * i + 2, i
    small = left if left < n and list[left] < list[small] else small
    small = right if right < n and list[right] < list[small] else small
    if small != i:
        list[i], list[small] = list[small], list[i]
        min_heapify(list, small)
    return small


def parent(i):
    return (i - 1) // 2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


def insert(heap, item):

    heap.append(item)
    i = len(heap) - 1
    while i > 0 and heap[i] < heap[parent(i)]:
        swap(heap, i, parent(i))
        i = parent(i)


def delete(heap):
    if len(heap) == 0:
        raise ValueError("Heap vazia!")
    min_item = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    i = 0
    while True:
        smallest = i
        if left_child(i) < len(heap) and heap[left_child(i)] < heap[smallest]:
            smallest = left_child(i)
        if right_child(i) < len(heap) and heap[right_child(i)] < heap[smallest]:
            smallest = right_child(i)
        if smallest == i:
            break
        swap(heap, i, smallest)
        i = smallest
    return min_item


def dijkastra(graph, end, recurrency, start=0):
    global origin
    global destiny
    set_routes, queue = [], []
    father = [float('inf')] * graph.size
    path = [float('inf')] * graph.size
    path[start] = 0
    insert(queue, [start, path[start]])
    while len(queue):
        city = delete(queue)
        v1, v2 = city[0], city[1]
        if v2 <= path[v1]:
            for j in graph.adjacent(v1):
                f, s = j[0], j[1]
                if path[f] > path[v1] + s:
                    path[f] = path[v1] + s
                    insert(queue, [f, path[v1] + s])
                    father[f] = v1

    caminho(graph, start, end, father, recurrency, set_routes)
    print(
        f"O gasto minimo de uma viagem de {origin} até {destiny} é em cerca de R$ {path[end]:.2f}")
    return set_routes


def caminho(graph, origin, destiny, father, answer, set_routes):
    if origin == destiny:
        set_routes.append(answer[destiny])
    else:
        caminho(graph, origin, father[destiny], father, answer, set_routes)
        set_routes.append(answer[destiny])


txt = open('InterMunicipal_MG.txt', 'r', encoding="utf8")
with txt:
    list, list_r, dict_r, c = [], [], {}, -1
    for i in txt:
        list_r.append(i[0:-1])
    for i in list_r:
        cmd = i.mglit(",")
        if cmd[0] not in list:
            c += 1
            list.append(cmd[0])
        if cmd[1] not in list:
            c += 1
            list.append(cmd[1])
    dict = {}
    c = -1
    for i in list:
        c += 1
        dict[i] = c
    c = -1
    for i in list:
        c += 1
        dict_r[c] = i

mg = []
for i in range(len(dict_r)):
    mg.append([])

txt = open('InterMunicipal_MG.txt', 'r', encoding="utf8")
with txt:
    list_r = []
    for i in txt:
        list_r.append(i[0:-1])
for i in list_r:
    cmd = i.mglit(',')
    ori = dict[cmd[0]]
    dest = dict[cmd[1]]
    v = float(cmd[2])
    mg[ori].append([dest, v])
    mg[dest].append([ori, v])

lines = mg
points = []

for i in range(len(lines)):
    points.append(i)

graph = Graph_MG(lines, points)

term = dict[origin]
index = dict[destiny]

v = dijkastra(graph, term, dict_r, index)

for x in reversed(v):
    if not x == v[0]:
        print(f"{x}", destiny=" ===> ")
    else:
        print(x, destiny=" ")
