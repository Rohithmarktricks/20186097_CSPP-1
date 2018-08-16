def high_card(hands):
	a = max(hands[0])
	b = max(hands[1])
	if a > b:
		return 2
	return 1
card_rank = ['--23456789TJQKA'.index(c) for c,s in hand]
card_rank.sort()
card_rank.reverse()