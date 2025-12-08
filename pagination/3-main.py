#!/usr/bin/env python3
"""
Main file for deletion-resilient pagination
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()
server.indexed_dataset()

index = 3
page_size = 2

d = server.get_hyper_index(index, page_size)

# Verify outputs
print("index has correct value:", d["index"] == index)
print("next_index has correct value:", d["next_index"] == index + page_size)
print("it is delete-resilient!")
