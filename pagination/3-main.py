#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

# Ensure the indexed dataset is built
server.indexed_dataset()

# Test out-of-range index
try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")

index = 3
page_size = 2

print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 1- request first page
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next page
print(server.get_hyper_index(res.get('next_index'), page_size))

# 3- remove the first index
del server._Server__indexed_dataset[res.get('index')]
print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -> first data is not the same as first request
print(server.get_hyper_index(index, page_size))

# 5- request again initial next index -> same data page as the previous next page
print(server.get_hyper_index(res.get('next_index'), page_size))
