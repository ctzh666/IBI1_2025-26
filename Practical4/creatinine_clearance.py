# 肌酐清除率计算器 - 伪代码规划
# 1. 获取用户输入：年龄、体重、性别、肌酐浓度
# 2. 将输入的字符串转换为数字
# 3. 验证所有输入是否在有效范围内：
#    - 年龄 < 100岁
#    - 20 kg < 体重 < 80 kg
#    - 0 < 肌酐浓度 < 100 μmol/l
#    - 性别是 ‘male‘ 或 ’female‘
# 4. 如果任一输入无效，打印错误信息并停止程序。
# 5. 如果所有输入有效，则应用Cockcroft-Gault公式计算 CrCl：
#    - CrCl = (140 - 年龄) * 体重 / (72 * Cr)
#    - 如果性别为女性，结果乘以 0.85
# 6. 打印计算结果。
age = int(input("age:" ))
weight = float(input("weight:" ))
gender = input("（male/female）:" ) 
cr = float(input("cr（μmol/l）: "))
if age >= 100 or age <= 0: 
    print("error")
    exit() 
elif weight <= 20 or weight >= 80:
    print("error")
    exit()
elif cr <= 0 or cr >= 100:
    print("error")
    exit()
elif gender not in ["male", "female"]:
    print("error")
    exit()
creatinine_clearance = (140 - age) * weight / (72 * cr)
if gender == "female":
    creatinine_clearance = creatinine_clearance * 0.85
print(str(creatinine_clearance) + " ml/min")