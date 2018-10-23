import csv
with open('demo1.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['ISBN','Title'])
    writer.writerow(['9730262510875','Structure and Interpretation of Computer Programs - 2nd Edition'])
