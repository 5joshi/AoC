from aocd import get_data
d = get_data(year=2023, day=4).splitlines()

# Part 1
# print(sum([int(2**~-len({l[:10]}&{l[10:]}))for l in[[int(x)for x in l.split()if x.isnumeric()]for l in d]]))
# print(sum([int(2**~-len({*l[:10]}&{*l[10:]}))for l in[[*map(int,(l[9:40]+l[42:]).split())]for l in d]]))
# print(sum([int(2**~-len(eval(f"{{{','.join(l[9:].replace('|','}&{0').split())}}}")))for l in d]))
# print(sum([int(2**~-len({*(w:=l.split())[2:12]}&{*w[13:]}))for l in d]))
# print(sum([int(2**(35-len({*(l.split())[2:]})))for l in d]))
# print(sum(2**(38-len({*(l.split())}))//2 for l in d))


print(sum(1<<37>>len({*l.split()})for l in d))

