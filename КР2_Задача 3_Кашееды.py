N = int(input())  
M = int(input())  
mannaya_lovers = {input().strip() for _ in range(N)}
ovcyanaya_lovers = {input().strip() for _ in range(M)}
all_lovers = mannaya_lovers & ovcyanaya_lovers
if all_lovers:
    print(len(all_lovers))  
else:
    print("Таких нет")
