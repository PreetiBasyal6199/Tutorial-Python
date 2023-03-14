# How to sort dictionary by value in Python?

markdict={"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
sorted_dict = dict(sorted(markdict.items(), key=lambda x: x[1]))
print(sorted_dict)