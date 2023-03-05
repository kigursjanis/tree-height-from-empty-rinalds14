import sys
import threading


def calculate_tree_height(n, parents):
    children = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            children[parent].append(i)
 
    def compute_depth(node):
        if not children[node]:
            return 1
        max_depth = 0
        for child in children[node]:
            depth = compute_depth(child)
            max_depth = max(max_depth, depth)
        return max_depth + 1

    return compute_depth(root)


def main():
    input_type = input()

    if 'I' in input_type:
        num_nodes = int(input())
        node_parents = list(map(int, input().split()))
        tree_height = calculate_tree_height(num_nodes, node_parents)
        print(tree_height)
    elif 'F' in input_type:
        file_name = input()
        with open("test/" + file_name, 'r') as f:
            num_nodes = int(f.readline())
            node_parents = list(map(int, f.readline().split()))
            tree_height = calculate_tree_height(num_nodes, node_parents)
            print(tree_height)
    else:
        print("invalid input")
        exit()



sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)  
threading.Thread(target=main).start()
