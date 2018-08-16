def royal_flush(hand):
	face_hand = []
    suit_hand = []
    for i in hand:
        face_hand.append(GOBAL_DICT[i[0]])
        suit_hand.append(i[1])
    face_hand.sort()
    suit_hand.sort()

    if len(set(suit_hand))==1:
    	if(len(set(face_hand)))==5:
    		return True
		return False