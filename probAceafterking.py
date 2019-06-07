
def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) 
    return round(probability, 3)
    #return round(probability, 1)

cards = 52
cards_drawn = 1
cards = cards - cards_drawn
aces = 4
# prob of drawing an ace after drawing a King
ace_probability1 = event_probability(aces, cards)
#prob drawing an Ace after drawing an Ace on the first draw
aces_drawn =1
aces = aces - aces_drawn
ace_probability2 = event_probability(aces, cards)
print(ace_probability1)
print(ace_probability2)