from datetime import datetime 
N = int(input())
format = '%a %d %b %Y %H:%M:%S %z'
for i in range(N):
    print(int(abs(datetime.strptime(input(),format) - 
                  datetime.strptime(input(),format)).total_seconds()))