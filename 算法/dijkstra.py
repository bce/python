#!狄克斯特拉算法
# -*- coding: UTF-8 -*-

import datetime

graph = {}#将所有节点存储到散列表中
graph['Start']={}
graph['Start']["A"]=5
graph["Start"]['B']=2
graph["A"]={}
graph["A"]["C"]=4
graph["A"]["D"]=2
graph["B"]={}
graph["B"]["A"]=8
graph["B"]["D"]=7
graph["C"]={};
graph["C"]["End"]=3
graph["C"]["D"]=6
graph["D"]={}
graph["D"]["End"]=1
graph["End"]={}
#graph = {'A': {'C': 4, 'D': 2}, 'Start': {'A': 5, 'B': 2}, 'C': {'End': 3, 'D': 6}, 'B': {'A': 8, 'D': 7}, 'D': {'End': 1}}

infinity = float('inf')
#存储节点权重的散列表
costs={"A":5,"B":2,"C":infinity,"D":infinity,"End":infinity}
#存储父节点的散列表
parents={"A":"Start","B":"Start","C":"A","D":None,"End":None}
processed=[]#处理过的节点

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

start = datetime.datetime.now()
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    print processed
    print costs
    if(node=="End"):
        break
print parents
end = datetime.datetime.now()
print (end-start)


            
    
