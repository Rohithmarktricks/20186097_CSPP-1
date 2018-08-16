def high_card(hands):
	a = max(hands[0])
	b = max(hands[1])
	if a > b:
		return 2
	return 1