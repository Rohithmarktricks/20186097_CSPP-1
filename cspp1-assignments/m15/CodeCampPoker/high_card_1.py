def high_card(hand):
	a = []
	if max(hand) > max(a):
		a.extend(hand)
		return True
	return False