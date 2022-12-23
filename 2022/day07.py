from utils import *

# inp = get_data(year=2022, day=7)

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        
    def get_subdir(self, name):
        for child in self.children:
            if child.name == name: return child
        
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        
    def size(self):
        return sum([child.size() for child in self.children])
    
class File:
    def __init__(self, name, file_size):
        self.name = name
        self.file_size = file_size

    def size(self):
        return self.file_size

def create_filesystem(d):
    inp = d.splitlines()
    root = Directory("root")
    curr_dir = root
    all_dirs = []
    
    for line in inp:
        line = line.split(" ")
        match line[0]:
            case "$":
                if line[1] == "ls": continue
                match line[2]:
                    case "/":
                        curr_dir = root
                    case "..":
                        curr_dir = curr_dir.parent
                    case name:
                        curr_dir = curr_dir.get_subdir(name)
            case "dir":
                new_dir = Directory(line[1], curr_dir)
                curr_dir.add_child(new_dir)
                all_dirs.append(new_dir)
            case size:
                new_file = File(line[1], int(size))
                curr_dir.add_child(new_file)    
        
    return root, all_dirs

def solve1(d):
    _, dirs = create_filesystem(d)
    return sum([directory.size() for directory in dirs if directory.size() < 100000])

def solve2(d):
    root, dirs = create_filesystem(d)
    space_needed = root.size() - 40000000
    return min([directory.size() for directory in dirs if directory.size() > space_needed])


s = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
s2 = """
"""

print("PART 1")
print("Example Solution:", solve1(s))
# print("Example 2 Solution:", solve1(s2))
# print("Actual Solution:", solve1(inp))

print("PART 2")
print("Example Solution:", solve2(s))
# print("Example 2 Solution:", solve2(s2))
# print("Actual Solution:", solve2(inp))
