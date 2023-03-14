# How to sort dictionary by value in Python?

markdict={"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
sorted_dict = dict(sorted(markdict.items(), key=lambda x: x[1]))
print(sorted_dict)

# How to merge dictionaries in Python?

d1={'A1': 20, 'B1': 25, 'C1': 40, 'D1': 50}
d2={"X1":100, "Y1":200, "b1":25, "A1":22,"D1":"Hello"}
for k,v in d2.items():
    d1[k]=v
print(d1)