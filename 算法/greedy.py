#!贪心算法greedy algorithm
# -*- coding: UTF-8 -*-

import datetime
import sys

print(sys.version)
stations = {}
stations["two"] = set(["wa","id","mt"])
stations["three"] = set(["or", "nv", "ca"])
stations["four"] = set(["nv", "ut"])
stations["five"] = set(["ca", "az"])
stations["one"] = set(["id","nv","ut"])
states_needed = set(["wa","mt","id","or","ca","nv","az","ut"])
#存储最终的集合
final_stations = set()
print (states_needed)
start = datetime.datetime.now()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        print station
        #print "states_needed:"+str(states_needed)
        #print "最 佳 best_station:"+str(best_station)+"  当 前 ："+str(station)
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
    print "finish one time"
print final_stations
end = datetime.datetime.now()
print (end-start)


            
    
