# コードが長くなりすぎる場合、（）で囲むか/で改行を入れる
x = 10

if x < 0:
    print('negative')
elif x == 10:
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
y = [1, 2, 3]
x = 1
if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2
if not a == b:
    print('not equal')

if a != b:
    print('not equal')

# is_ok = True
# if is_ok:
#     print('hello')
# is_ok = True

# 変数に値が入っていれば、trueと判定する　整数０だとfalse
# is_ok = 1
is_ok = 's'
if is_ok:
    print('OK')
else:
    print('NO!')
# pythonではデータが入っていない状態をnoneとする　Nonetypeのクラスも存在する
# 変数を宣言して、何も入れていない
# if is_empty == None はpy的に好ましくない
# if is_empty is None:
# print('none!')

# count = 0
# while count < 5:
#     print(count)
#     count += 1
count = 0
while True:
    print('XXX')
    if count >= 5:
        # breakはループから完全に抜ける 今回は４まで抜けるとカウントから抜ける
        break
    if count == 2:
        count += 1
        # continueは次のコードに進まず、次のループに進む
        # 今回は、２をスキップして３のカウントに飛ぶ
        continue
    print(count)
    count += 1

#
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')

# inputで文字を入力できるようにする。
# 今回は、if で宣言した内容と入力が一致するとループを抜ける仕組み
while True:
    word = input('Enter:')
    # if word = 'ok':
    num = int(word)
    # if word =='ok':
    if num == 100:
        break
    print('next')