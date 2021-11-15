def hidecard(card):
    cardl = list(str(card))
    cardl[0:12] = "**** **** **** "
    hidden = "".join(map(str, cardl))
    return hidden

card = 5326658966336525

print (hidecard(card))


