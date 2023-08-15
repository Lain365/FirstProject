'''
Created on 2023/08/15

@author: lain
'''
from random import randint

# た行一覧
wordList = ['た', 'ち', 'つ', 'て', 'と']

# 成功回数（ありがちんちんだった数）
successCount = 0

# 試行回数
trialCount = 10

def wordMake():
    """
    ありがXんXんを作成し表示
    """
    global successCount
    firstWord = wordList[randint(0,4)]
    secondWord = wordList[randint(0,4)]
    separateWord = 'ん'
    result = f'ありが{firstWord + separateWord + secondWord + separateWord}'
    if (result == 'ありがちんちん'):
        successCount += 1
    print(result)

for i in range(trialCount):
    wordMake()

print(successCount, '/', trialCount)