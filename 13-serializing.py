import pickle

cities = ["moskova","berlin","tokyo","paris"]

"""
with open("pickle/cities.bin", "wb") as fileObject:
    pickle.dump(cities, fileObject)  # citiesi
"""

with open("pickle/cities.bin","rb") as fileObject:
    cities = pickle.load(fileObject)
    print(cities)

cities.append("Istanbul")
print(cities)


with open("pickle/cities.bind","wb") as fileObject:
    pickle.dump(cities,fileObject)


