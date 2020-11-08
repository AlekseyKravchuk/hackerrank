#  Build a list of Unicode codepoints from a string
symbols = '$¢£¥€¤'
chinese = '比艾弗'
ascii_str = 'abcd'

ranks = ['A', 'K', 'Q']
suits  = ['♠', '♥', '♦', '♣']
pack = [(rank, suit) for rank in ranks for suit in suits]
for i in pack:
    print(f'{i}, {()}, type = {type(i)}')