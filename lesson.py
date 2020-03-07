# 変数の最初に数字を入れるとエラーになる
num = 1
name = 'Mike'
print(num,type(num))
print(name,type(name))
# pythonでは型数を宣言する必要はない
# 変数typeは型の形式を表示させる
ab = 1
ac = "Michael"
ab = ac
print(ab,type(ab))
#型の変換コード　alphaは今文字列の１
alpha = '1'
print(alpha)
# intを宣言することで整数型に変更できる
new_num = int(alpha)
print(new_num, type(new_num))
# 実行結果→整数が表示された。
print('Hi', 'Mike')
# これだとカンマがスペースとして表示される
print('Hi', 'Mike',sep=',')
# sep=の引数のカンマを置くとカンマが区切りとして表示される。
print('Hi', 'Mike',sep=',', end='.\n')

# ここら辺はRubyでやったやつと変わらない
print(2 + 2)
print(4 - 2)
print(6 * 5)
print(10 / 5)
print(17 % 3)
print(50 - 5 * 6)
print((50 - 10) * 6)
print(8 / 5)
print(17 / 3)
# コンピューターの近似値（なにそれ？）まで出す
print(17 // 3)
#商を表示（この言い方久々）
print(5 * 5)
print(5**2)
# 乗の計算ができる
x = 10
y = 5
print(x * y)
ak74 = 5.45555
print(round(ak74, 2))
ak47 = 7.6222222
print(round(ak47, 2))
# roundは表示させる少数点指定する。なお最後の数字は小数点となる？
# import math を書き　math.＊＊＊＊で数学関数を入れられる。
# print(heap(math))で数学関数の説明と一覧が出てくる
print("I don't know")
print('I don\'t know')
# \で囲んでいるシングルクオートとそうでないシングルクオートを差別化できる
print("say \"I don't know\"")
# ダブルクオートも同じく
print('Hello. \nHow are you?')
# 　\nは改行の際に使う
print('c:\name\name')
# パス指定の際、\nがあるとameと表示されてしまう。
print(r'c:\name\name')
# その場合、rを付けると正しく表示させることができる。
print("#############")
print("""\
line1
line2
line3\
""")
print("############")
# ダブルクオート分の改行が行われる。 \で改行しつつコードを続けることができる。
word = 'python'
print(word[0])
print(word[-1])
print(word[3])
# wordの引数のn番目の文字を表示させた。
print(word[0:2])
print(word[2:5])
#wordの引数のn0~n2までとn2~n5番の文字を表示させた。
print(word[:2])
print(word[:6])
# 最初と最後の指定を省略できる
word = 'j' +  word [1:]
print(word)
#変数を宣言して、入れたい言葉＋言葉のn番を指定して代入しました
n = len(word)
print(n)
#関数lenで変数の文字列を出した。
s = "my name is Mike. Hi Mike."
is_start = s.startswith('my')
are_start = s.startswith('are')
print(is_start)
print(are_start)
#関数startwithで'my'を指定　変数sの内容がmyで始まっているのでtrue
#関数startwithで'my'を指定　変数sの内容がmyで始まっているのでfalse
print(s.find('Mike'))
print(s.rfind('Mike'))
# 関数findは変数s内の指定された値がある場所を探す. Mikeは１１文字目にある
# rfindは指定された値が最後に出てくる場所を探す今回は2回目のMikeは２０番目
print(s.count('Mike'))
# 関数countは指定された値の個数をカウントする
print(s.capitalize())
# 関数capitalizeは指定された値（今回は文字列全体）の最初の文字を大文字に
print(s.title())
# 関数titleは指定された値（今回は各単語の）の最初の文字を大文字に
print(s.upper())
# 関数upperは指定された値のすべての文字を大文字に
print(s.lower())
# 関数lowerは指定された値のすべての文字を小文字に
print(s.replace('Mike', "Nancy"))
# 関数replaceは指定された値に別の文字列を代入する
# 以下コンソールで試したこと
# 'a is {}' .format('test')
# 'a is test'
# 'a is {} {} {}' .format(1, 2, 3)
# 'a is 1 2 3'
# 'a is {2} {1} {0}' .format(1, 2, 3)
# 'a is 3 2 1'
# 'my name is {0} {1}'.format('S', 'Mike')
# 'my name is S mike'
# 'my name is {0} {1}. watashi ha {1} {0}'.format('S', 'Mike')
# 'my name is S Mike. watashi ha Mike S '
# 数字は変数に帰ることもできる
# 'my name is {name} {familly}'.format(name='S', family='Mike')