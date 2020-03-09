# コードが長くなりすぎる場合、（）で囲むか/で改行を入れる
x = 0

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')

a = 5
b = 10
# pythonのインデントは条件が厳しい、即エラーになる
if a > 0:
    print('positive')
    if b > 0:
        print('b is positive')