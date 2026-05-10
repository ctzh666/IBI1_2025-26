import re
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
orf = re.findall(r'AUG.+?(?:UAA|UAG|UGA)',seq)
print("All matched ORFs:")
print(orf)
if orf:
    longest_orf = max(orf, key=lambda x: len(x))
    longest_len = len(longest_orf)
    print("\nLongest ORF sequence:", longest_orf)
    print("Longest ORF nucleotide length:", longest_len)
else:
    print("\nNo ORFs were found")
