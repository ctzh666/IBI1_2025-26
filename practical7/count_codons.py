import matplotlib.pyplot as plt
fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'  # 请确保文件在这
valid_stops = ['TAA', 'TAG', 'TGA']
while True:
    target_stop = input(f"({', '.join(valid_stops)}): ").upper().strip()
    if target_stop in valid_stops:
        break
genes = {} 
current_id = None
current_seq_parts = []
with open(fasta_file, 'r') as f:
     for line in f:
        line = line.strip()
        if not line:
             continue
        if line.startswith('>'):
            if current_id is not None:
                    genes[current_id] = ''.join(current_seq_parts)
            header = line[1:]
            current_id = header.split(';')[0]
            current_seq_parts = []
        else:
            current_seq_parts.append(line)
print(f"number= {len(genes)} ")
all_codon_counts = {} 
genes_with_valid_orf = 0
for gene_name, seq in genes.items():
    longest_orf_for_this_gene = ""  
    longest_length = 0
    for frame in range(3):
        i = frame  
        while i < len(seq) - 2: 
            if seq[i:i+3] == 'ATG': 
                start = i
                j = i + 3  
                while j < len(seq) - 2:
                    current_codon = seq[j:j+3]
                    if current_codon == target_stop:
                        orf_seq = seq[start:j]  
                        if len(orf_seq) > longest_length:
                            longest_length = len(orf_seq)
                            longest_orf_for_this_gene = orf_seq
                        break  
                    elif current_codon in ('TAA', 'TAG', 'TGA'):
                        break
                    j += 3  
            i += 3 
    if longest_orf_for_this_gene:
        genes_with_valid_orf += 1
        orf_seq = longest_orf_for_this_gene
        for k in range(0, len(orf_seq), 3):
            a_codon = orf_seq[k:k+3]
            if len(a_codon) == 3: 
                if a_codon in all_codon_counts:
                    all_codon_counts[a_codon] += 1
                else:
                    all_codon_counts[a_codon] = 1
print(f"\nfinish")
print(f"in{len(genes)} genes,there are{genes_with_valid_orf} have '{target_stop}'ORF")
if not all_codon_counts:
    print("no")
    exit()
total_codons = sum(all_codon_counts.values())
print(f"there are {total_codons} ")
print("\nfrom most to least:")
sorted_list = sorted(all_codon_counts.items(), key=lambda x: x[1], reverse=True)
for codon, count in sorted_list:
    print(f"  {codon}: {count}")
pie_labels = []
pie_sizes = []
for codon, count in sorted_list:
    pie_labels.append(codon)
    pie_sizes.append(count)
plt.figure(figsize=(12, 8))
wedges, texts, autotexts = plt.pie(pie_sizes, labels=pie_labels, autopct='%1.1f%%', startangle=140)
plt.title(f'the stops"{target_stop}" n(from {genes_with_valid_orf} genes, in all:{total_codons} )')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
plt.axis('equal')
output_pic_name = f'codon_pie_for_stop_{target_stop}.png'
plt.tight_layout()
plt.savefig(output_pic_name, dpi=300)
print(f" {output_pic_name}")
plt.show()