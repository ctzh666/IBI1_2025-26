import re
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
orf=re.findall(r'AUG.+?(?:UAA|UAG|UGA)',seq)
print(orf)
print("orf number:", sum(len(n) for n in orf) )