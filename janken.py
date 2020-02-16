import random
hand = ["グー","チョキ","パー","終了"]

# じゃんけんの繰り返し
while True:
	com = random.randint(0,2)
	for i,desc in enumerate(hand): # enumerate関数でインデックス番号と手を取得
		print(i, ":" , desc) # 手と数字の関係を出力
	you = int(input("出す手を数値で入力: "))
	if you == 3: 
		print("ゲーム終了、またやろうね。")
		break
	if you < 0 or you > 2:
		print("0か3の間で入力してね")
		continue
	
	# 手を表示
	print("自分:", hand[you])
	print("相手:", hand[com])
	
	j = (you - com + 3) % 3
	if j == 0 :
		print("あいこ")
	elif j == 1:
		print("負け")
	else:
		print("勝ち")
		