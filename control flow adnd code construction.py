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
# while True:
#     word = input('Enter:')
#     # if word = 'ok':
#     num = int(word)
#     # if word =='ok':
#     if num == 100:
#         break
#     print('next')

some_list = [1, 2, 3, 4, 5]
for i in some_list:
    print(i)
for s in 'abcdef':
    print(s)
for n in ['my', 'name', 'is', 'John']:
    print(n)

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all')
# range　関数 (開始する数字、カウントする数字数、何個とばし）
for xx in range(2, 10):
    print(xx, 'hello')
i = 0
# enum
for i, fruit in enumerate(['banana', 'apple', 'orange']):
    print(i, fruit)

# zip
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffe', 'tea', 'beer']
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# dictのforメソッド　よく使う！！　kはkeys, vはvalueの略　itemsで各要素のキーと値に対してfor処理をする
d = {'x': 100, 'y': 200}
for k, v in d.items():
    print(k, ':', v)


# 関数定義(function)
def say_something():
# say_something()
# f = say_something
# f()
    s = 'hi'
    return s
result = say_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"
result = what_is_this('green')
print(result)

def menu(entree, drink, desert):
    print(entree)
    print(drink)
    print(desert)
menu(entree='beef', desert='beer', drink='ice')

def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

def say_something(word, *args):
    print(word)
    for arg in args:
        print(arg)
say_something('hi', 'mike', 'nace')

def menu2(**kwargs):
    #print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
#d = {
 #   'entree':'beef',
 #  'drink': 'ice coffee',
 # 'dessert':'ice'
#}
menu2(**d)
#menu2(entree='beef', drink='coffee')

