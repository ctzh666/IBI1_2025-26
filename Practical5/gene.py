import matplotlib.pyplot as plt
genes_dic = {'TP53' : 12.4 , 'EGFR' : 15.1 , 'BRCA1' : 8.2 , 'PTEN' : 5.3 , 'ESR1' : 10.7}
genes_dic['MYC'] = 11.6
genes = list(genes_dic.keys())
expressions = list(genes_dic.values())
plt.figure(figsize=(10,6))
bars = plt.bar(genes,expressions,color='skyblue')
plt.title("genes and expressions", fontsize=16, fontweight='bold')
plt.xlabel("genes", fontsize=12)
plt.ylabel("expressions", fontsize=12)
for bar, value in zip(bars, expressions):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.1,
             f'{value}', ha='center', va='bottom', fontsize=10)
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.ylim(0, max(expressions) * 1.15)
plt.tight_layout()
plt.show()
interest = "TP53"#you can change the name of gene here
if interest in genes_dic:
    print(genes_dic[interest])
else:print("error")
expression = list(genes_dic.values())
average = sum(expression)/len(expression)
print ("the average is:", average)