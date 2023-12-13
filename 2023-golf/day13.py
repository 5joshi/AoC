from aocd import get_data
d = get_data(year=2023, day=13).split('\n\n')


# PART 1

e=lambda r:[i for i in range(len(r))if all(x==y for x,y in zip(r[i:],r[:i][::-1]))][-1]
print(sum(100*e(r:=[*map(list,g.split('\n'))])or e([*zip(*r)])for g in d))


# PART 2

e=lambda r:([i for i in range(len(r))if sum(sum(a!=b for a,b in zip(x,y)) for x,y in zip(r[i:],r[:i][::-1]))==1]or[0])[-1]
print(sum(100*e(r:=[*map(list,g.split('\n'))])or e([*zip(*r)])for g in d))