heart_rates	= [72,60,126,85,90,59,76,131,88,121,64]
print ("number=", len(heart_rates))	
average = sum(heart_rates)/len(heart_rates)
print ("average=", average)
i = 0
low = 0
normal = 0
high = 0
while i < len(heart_rates):
    if heart_rates[i]<60:
        low=low+1
    elif heart_rates[i]>=60 and heart_rates[i]<=120:
        normal=normal+1
    elif heart_rates[i]>120:
        high=high+1
    i=i+1
print("low=", low,";normal=", normal,";high=", high)
if low>normal and low>high:
    print("the most is low")
elif normal>low and normal>high:
    print("the most is normal")
elif high>low and high>normal:
     print("the most is high")

import matplotlib.pyplot as plt
categories = ['Low (<60)', 'Normal (60-120)', 'High (>120)']
counts = [low, normal, high]  
colors = ['lightblue', 'lightgreen', 'salmon']  
plt.figure(figsize=(8, 6))
wedges, texts, = plt.pie(
    counts,
    labels=categories, 
    startangle=90,      
    colors=colors
)
for text in texts:
    text.set_fontsize(12)
plt.title('Heart Rate Categories Distribution', fontsize=14, fontweight='bold', pad=20)
legend_labels = [f'{cat}: {count} patients' for cat, count in zip(categories, counts)]
plt.legend(wedges, legend_labels, title="Category Counts", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.axis('equal')
plt.tight_layout()
plt.show()