# pythonと配列
from typing import List

l = [1, 2, 3, 5, 7, 11]
print(l[3])
print(l[0:2])
print(l[2:])
print(l[:2])
print(l[-2])
print(l[-2:])
print(l[:-2])
print(l[2:7])
print(len(l))

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
# ２つ飛ばしのやり方
print(n[::-1])
a = ['a', 'b', 'c']
b = [1, 2, 3]
x = [a, b]
print(x)
print(x[0][2])
print(x[1][0])
# 配列を代入でき、その内容を指定して出力する方法

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)
s[0] = 'x'
# s[0]にｘを代入
print(s)
s[2:5] = ['C', 'D', 'E']
print(s)
# s[2:5]の配列に代入
s[2:5] = []
print(s[:])
# 空の[]を代入すると、配列から削除される

w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(w)
w.append(25)
w.insert(1, 21)
print(w)
# 関数append配列の最後に値を代入
# insertは指定個所に値を代入
w.pop(0)
print(w)
# 関数popは指定された場所の値を配列から取り除く。指定しないと最後の要素を削除
del w[0]
print(w)
# 関数delは指定された場所の値を配列から取り除く。
# del ステートメントは削除された値を返さない
# 例えば、 del w を実行すると変数自体が削除される
list = ['Mike', 'Alex', 'Francis']
list.remove('Alex')
print(list)
# removeは配列内の特定の値を削除する（今までは配列の場所を指定していた）
z = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
# k = z + y
# print(k)
z += y
print(z)
# x.extend(y)
r = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 10]
print(r.index(3))
# .indexは指定した値のある場所を選択する
print(r.count(3))
#  .indexは指定した値の個数を選択する
r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)
j = 'My name is Mike.'
to_split = j.split(' ')
print(to_split)
# 順番を変える関数

h = [1, 2, 3, 4, 5]
c = h
h[0] = 100
print('h =', h)
print('h =', c)
g = [1, 2, 3, 4, 5]
q = g.copy()
q[0] = 100
print(g)
print(q)

t = (1, 2, 3, 3, 4, 5)
# tupleは基本的に代入などができない　Append スライスといった関数は使える。
# 読み込み専用の配列として使うことが多い
t = ([1, 2, 3], [4, 5, 6])
print(t[0][0])
(t[0][0]) = 100
print(t[0][0])
# ただし上記のようなことはできる。
# t = 1, カンマがあるとtuple型になる　バグの原因になりやすい
# int + tpl はできない
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
x, y = 10, 20
print(x, y)

min, max = 0, 100
print(min, max)
# tuple要素が長くなりすぎる場合、

o = 10
p = 20
tmp = o
o = p
p = tmp
print(o, p)
# これが普通の入れ替え方

rev1 = 100
rev2 = 200
rev1, rev2 = rev2, rev1
print(rev1, rev2)
# tupleを使った入れ替え
# dictionally 型
d = {'xx' : 10, 'yy': 20}
print(d)
print(d['xx'])
d['xx'] = 'xxxxx'
d['z'] = 200
d[0] = 123
print(d)
# dictの関数は.keys(値)value（値についている内容）
# update関数で数字をオーバーライドあるいは追加が可能
ex = {'a': 1}
ey = ex
ey['a'] = 1000
print(ex)
print(ey)

ax = {'a':1}
bx = ax.copy()
bx['a'] = 1000
print(ax)
print(bx)

# dictの使い方
fruit = {
    'apple': 100,
    'banana' :200,
    'orange' :300,
}
print(fruit['banana'])
# キーに値が結びついているので、参照が早い

# set型（就業）
tx = {1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5}
print(tx)
sx = {2, 2, 3, 3, 5, 7, 8}
print(sx)
wx = tx - sx
print(wx)
cx = sx - tx
print(cx)
vv = tx & sx
print(vv)
nb = tx | sx
print(nb)
# add関数でdict配列に追加できる　removeで削除　clear中身を削除
# eg) 集合はSNSにて共通点を見つけ出すときに使える
my_friends = {'a', 'b', 'd',}
A_friend = {'d', 'c', 's'}
print(my_friends & A_friend)