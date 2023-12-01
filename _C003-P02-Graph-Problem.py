#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import pandas as pd 
import numpy as np 
data=pd.read_csv(r'C:\Users\Mallika Yeturi\OneDrive\Desktop\city_data.csv')

class System:
    steps = [   
        [-1,0], # Top Step
        [0,1],  # Right Step
        [1,0], # Bottom Step
        [0,-1] # Left Step
    ]
    
    def __init__(self):
        self.star_city = list()
        self.star_city_rows = 0
        self.star_city_cols = 0
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.reader(data_file)
        self.star_city = list()
        for row in reader:
            self.star_city.append(row)
        self.star_city_rows = len(self.star_city)
        self.star_city_cols = len(self.star_city[0])

    def check_limits(self, row_num, col_num):
        if 0 <= row_num < self.star_city_rows and 0 <= col_num < self.star_city_cols:
            return True
        return False

    def get_neighbours(self, row, col):
        neighbours = []
        #loop through top, right, bottom and left adjacent nodes to get the neighbor
        # only if the altitude of adjacent node is lower or equal to the current node 
        # and is not already present in neighbors list
        for i in System.steps:
            if self.check_limits(row+i[0], col+i[1]):
                if self.star_city[row+i[0]][col+i[1]] <= self.star_city[row][col] and (row+i[0], col+i[1]) not in neighbours:
                    neighbours.append((row+i[0], col+i[1]))
        return neighbours
    def find_route(self, source, destination):
        # empty que and visited lists
        que = []
        visited = []
        # add 1st node in visited and que lists
        start = [source]
        que.append(start)
        visited.append(start)

        # traverse all the nodes from que till the que is not empty
        # or destination is not found
        while que:
            # get the first path from que and mark it visited
            path = que.pop(0)
            last_node = path[-1]

            # get the last node from the visited path
            row, col = last_node

            # if the last node from visited path is destination then return the visited path
            if last_node == destination:
                return path

            # get each neighbours of the last node one by one
            neighbours = self.get_neighbours(row, col)
            for neighbour in neighbours:
                # if neighbour is not visited then make a new path with the existing nodes from visited list and the neighbour
                # and add the new path in que
                if neighbour not in visited:
                    new_path = list(path)
                    new_path.append(neighbour)
                    que.append(new_path)
                    visited.append(neighbour)

        # return empty list if path not found
        return []

    def Bluevalley_to_Smallville_route(self):
        # row number and column number of Source city i.e., Bluevalley
        source = (3, 0)

        # row number and column number of Destination city i.e., Smallville
        destination = (3, 4)

        # flag indicating route not found initially
        found = False

        # find the route from Bluevalley to Smallville
        route = self.find_route(source, destination)

        # if route is non-empty so display the route and mark the flag as found and break
        if route:
            print("\n\nTo reach city Smallville from city Blue Valley the nodes traversed are-")
            for nodenum, node in enumerate(route):
                if nodenum != len(route) - 1:
                    print(f"({node[0]}, {node[1]}) ---->", end=" ")
                else:
                    print(f"({node[0]}, {node[1]})", end=" ")
            found = True
            
        # if flag set to found, stop finding further routes
        if not found:
            print("\n\nRoute from Bluevalley to Smallville not found")

        
if __name__ == "__main__":
    test_system1 = System()
    
    #Getting data in 2D matrix
    test_system1.config_system('city_data.csv')
    
    #Finding path between Source node to Destination node
    route = test_system1.find_route((3,0),(4,2))
    print(f"\n\nTo reach Node (4,2) from Node (3,0) the nodes traversed are-")
    for nodenum, node in enumerate(route):
        if nodenum != len(route)-1:
            print(f"({node[0]}, {node[1]}) ---->", end=" ")
        else:
            print(f"({node[0]}, {node[1]})", end=" ")
    
    #Finding path between Bluevalley to Smallville   
    test_system1.Bluevalley_to_Smallville_route()


# In[ ]:





# In[ ]:




