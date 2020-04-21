# filepath = 'Basic.txt'
# names = []
# with open(filepath) as fp:
#    lines_list = fp.read().splitlines()()
#    print(lines_list,"List")
   # cnt = 1
   # while line:
   #     #print("Line {}: {}".format(cnt, line.strip()))
   #     names = line.strip()
   #     #line = fp.readline()
   #     cnt += 1

lines_list = open('Basic.txt').read().splitlines()
for i in lines_list:
    List = (i.split(','))
    print(List)
    print(List[1])
