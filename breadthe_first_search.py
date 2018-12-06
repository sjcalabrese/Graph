from graph import Graph
from python_queue import Queue
from word_ladder import *

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == "white"):
                nbr.setColor("Gray")
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
            currentVert.setColor("black")

def traverse(y):
    x = y
    while(x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())
    
    
    
def main():
    file = "words.txt"
    graph = buildGraph(file)
    for g in graph:
        for w in g.getConnections():
            print("{0} , {1}".format( g.getId(), w.getId()))
    bfs(graph, [0])    
main()
