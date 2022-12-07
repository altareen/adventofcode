###
#-------------------------------------------------------------------------------
# spacedevice.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 07, 2022
# Execution:    python3 spacedevice.py
#
# This program determines the sum of the directories of size <= 100000.
#
##

from anytree import Node, RenderTree, PreOrderIter

# generate the directory tree
def generate_tree(terminal):
    directories = []
    for command in terminal:
        if command.startswith('$ cd'):
            name = command.split()[-1]
            if name == '/':
                root = Node('root')
                directories.append(root)
            elif name == '..':
                directories.pop()
            else:
                directories.append(Node(name, parent=directories[-1]))
        elif not (command.startswith('$') or command.startswith('dir')):
            name = command.split()[-1]
            name = Node(command, parent=directories[-1])
    return root

# part one
def space(data):
    with open(data, 'r') as f:
        entries = f.readlines()

    terminal = [item.strip() for item in entries]
    root = generate_tree(terminal)

    # display the directory tree
#    for pre, fill, node in RenderTree(root):
#        print("%s%s" % (pre, node.name))

    total = 0
    result = [node for node in PreOrderIter(root) if len(node.name.split()) == 1]
    for item in result:
        outcome = [node.name for node in PreOrderIter(item)]
        current = 0
        for entity in outcome:
            if len(entity.split()) > 1:
                current += int(entity.split()[0])
        if current <= 100000:
            total += current

    return total

# part two
def device(data):
    with open(data, 'r') as f:
        entries = f.readlines()
    
    terminal = [item.strip() for item in entries]
    root = generate_tree(terminal)

    used_space = 0
    outcome = [node.name for node in PreOrderIter(root)]
    for entity in outcome:
        if len(entity.split()) > 1:
            used_space += int(entity.split()[0])
    free_space = 70000000 - used_space
    required_size = 30000000 - free_space

    smallest = 30000000
    result = [node for node in PreOrderIter(root) if len(node.name.split()) == 1]
    for item in result:
        outcome = [node.name for node in PreOrderIter(item)]
        current = 0
        for entity in outcome:
            if len(entity.split()) > 1:
                current += int(entity.split()[0])
        if current >= required_size and current < smallest:
            smallest = current

    return smallest

# display puzzle answers
def main():
    print(f'[space] sample result: {space("sampledata.txt")}')
    print(f'[space] entire result: {space("entiredata.txt")}')
    print(f'[device] sample result: {device("sampledata.txt")}')
    print(f'[device] entire result: {device("entiredata.txt")}')

if __name__ == '__main__':
    main()
