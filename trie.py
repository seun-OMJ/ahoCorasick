#--------------------------------------------
# NAME: SEUN OMOJOLA
# STUDENT NUMBER: 7880480 
# COURSE: COMP 4820
#---------------------------------------------

class TrieNode:
    def __init__(self):
        self.children = {}
        self.output = [] 
        self.failure_link = None

def build_prefix_trie(list):
    root = TrieNode()  
    for string in list:
        node = root
        for char in string:
            if (char not in node.children):
                node.children[char] = TrieNode()
            node = node.children[char]
        node.output.append(string) 

    return root

def build_failure_links(root):
    queue = []
    root.failure_link = root
    queue.append(root)
    
    while queue:
        current_node = queue.pop(0)
        
        for char, child_node in current_node.children.items():
            if current_node == root:
                child_node.failure_link = root
            else:
                failure = current_node.failure_link
                while (failure != root) and (char not in failure.children):
                    failure = failure.failure_link
                if (char in failure.children):
                    child_node.failure_link = failure.children[char]
                else:
                    child_node.failure_link = root
            child_node.output += child_node.failure_link.output
            queue.append(child_node)

def search(seq, array, root):  

    node = root
    occurrences = {index: 0 for index in array} 

    for char in seq:
        while (node != root) and (char not in node.children):
            node = node.failure_link
        if (char in node.children):
            node = node.children[char]
        for pattern in node.output:
            occurrences[pattern] += 1

    return occurrences
 