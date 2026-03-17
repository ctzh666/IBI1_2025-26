import matplotlib.pyplot as plt
countries = ["英国", "中国", "意大利", "巴西", "美国"]
pop_2020 = [66.7, 1426, 59.4, 208.6, 331.6]  
pop_2024 = [69.2, 1410, 58.9, 212.0, 340.1]  
percentage_changes = []
for i in range(len(countries)):
    change = ((pop_2024[i] - pop_2020[i]) / pop_2020[i]) * 100
    percentage_changes.append(change)
print("change")
for i, country in enumerate(countries):
    print(f"{country}: {percentage_changes[i]:.2f}%")
sorted_data = sorted(zip(countries, percentage_changes), key=lambda x: x[1], reverse=True)
sorted_countries = [item[0] for item in sorted_data]
sorted_changes = [item[1] for item in sorted_data]
print("from the biggest increasing to the biggest decreasing")
for country, change in sorted_data:
    print(f"{country}: {change:.2f}%")
max_growth_country, max_growth = sorted_data[0]
max_decline_country, max_decline = sorted_data[-1]
print(f"increasing most: {max_growth_country} ({max_growth:.2f}%)")
print(f"decreasing most: {max_decline_country} ({max_decline:.2f}%)")
plt.figure(figsize=(12, 7))
bars = plt.bar(countries, percentage_changes, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
for bar, change in zip(bars, percentage_changes):
    height = bar.get_height()
    va = 'bottom' if change >= 0 else 'top'
    color = 'green' if change >= 0 else 'red'
    plt.text(bar.get_x() + bar.get_width()/2, height + (0.2 if change >= 0 else -0.2),
             f'{change:.2f}%', ha='center', va=va, fontsize=11, fontweight='bold', color=color)
plt.title('2020-2024 change of population',fontsize=16, fontweight='bold', pad=20)
plt.xlabel('country', fontsize=12)
plt.ylabel('percentage', fontsize=12)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.7)
plt.grid(axis='y', alpha=0.3, linestyle='--')
max_change = max(percentage_changes)
min_change = min(percentage_changes)
plt.ylim(min_change - 1, max_change + 1)
plt.tight_layout()
plt.show()