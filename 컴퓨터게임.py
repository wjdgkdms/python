import random



print('기회는 5번입니다')
print('범위를 입력하세요')

bum = int(input())
com = random.randint(1,bum)
    
for guessTaken in range(1, 5):
    print('예상하는 수를 입력해주세요')
    num = int(input())
    
    if com > bum :
        print('다시 입력해주세요')
        
    if num < com:
        print('UP')
        
    elif num > com:
        print('DOWN')     
           
    else:
        break
if num == com:
    print(str(com) + '는 정답입니다.')
else:
    print( '틀렸습니다' + str(com) + '입니다.')
