import os
import json

class Tree:
    def __init__(self, label, children):
        self.label = label
        self.children = children
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
def list2tree(cur_path):
    if os.path.isdir(cur_path):
        cur_file_list = os.listdir(cur_path)
        cur_children = []
        for dir in cur_file_list:
            path = cur_path+'\\'+dir
            cur_children.append(list2tree(path))
        return Tree(cur_path,cur_children) 
    else:
        return Tree(cur_path,[])