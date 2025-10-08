runs = {"virat": 29,"rohit": 68,"hardik":45}
print(runs, type(runs))
print(runs["hardik"])
runs["virat"] = 89#it is changeble.
print(runs.keys())#this will give you the keys.
print(runs.values())#this will give you values.
runs.clear
runs.pop("virat")#it will remove virat
print(runs)