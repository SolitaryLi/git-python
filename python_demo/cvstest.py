import csv

with open('cvstest.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age']) # 内部方法 writerow编辑器无提示

    
