# import random 
# import pCard

# def main ():
#     deck_of_cards = []
#     ranks = ['2', '3', '4', '5', '6', '7', '8', '9', "10", "jack", "queen", "king", "ace"]

#     suits = ["spades", "hearts", "clubs", "diamonds"]
#     for i in ranks: 
#         for j in suits:
#             c = pCard.playing_card(i, j)
#             deck_of_cards.append(c)
#     poker_hand = random.sample(deck_of_cards, 5)
#     poker_hand.sort(key = lambda x: x.get_rank())
#     for k in poker_hand:
#         print(k)

# main()

import math


lat1 = 40.721319
lat2 = 40.712278
long1 = -73.844311
long2 = -73.84161


distance = (((lat1-lat2)**2+(long1- long2)**2)**0.5)
print(distance)


# def euc_distance(lat1, lat2, long1, long2):
#     return(((lat1-lat2)**2+(long1- long2)**2)**0.5)
# print(euc_distance)




