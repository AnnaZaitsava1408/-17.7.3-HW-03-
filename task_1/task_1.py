money=int(input("Сумма под процeнты "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit_TKB=int(money/100*per_cent['ТКБ'])
deposit_SKB=int(money/100*per_cent['СКБ'])
deposit_BTB=int(money/100*per_cent['ВТБ'])
deposit_SBER=int(money/100*per_cent['СБЕР'])
deposit=[deposit_TKB, deposit_SKB, deposit_BTB, deposit_SBER]
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
