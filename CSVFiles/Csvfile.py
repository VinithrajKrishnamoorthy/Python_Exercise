import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file',help="File path")
args = parser.parse_args()
file = open('sample.json','w')
file1 = open(args.file,'r') 
reader = file1.readlines()
header_list=[]
header_list= reader[0].strip().split(',')
data = {}
for row in reader[1:]:
    row = row.strip().split(',')
    data.update({header_list[0]:row[0], header_list[1]:row[1], header_list[2]:row[2], header_list[3]:row[3], header_list[4]:row[4], header_list[5]:row[5], header_list[6]:row[6], header_list[7]:row[7], header_list[8]:row[8]})
    print(data)
    file.write(json.dumps(data,indent=4))
