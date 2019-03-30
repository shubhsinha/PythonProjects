import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append((suit, rank))
        random.shuffle(self.cards)

    def __str__(self):
        d = ""
        for a, b in self.cards:
            d += f"\n{b} of {a}"
        return "The shuffled deck has :" + d


class Choose:
    def __init__(self, deck, hand):
        self.hand = hand
        self.value = 0
        self.add_card = deck.cards.pop()
        self.hand.append(self.add_card)
        for suit, rank in self.hand:
            self.value += values[rank]
        for suit, rank in self.hand:
            if self.value > 21 and rank == 'Ace':
                self.value -= 10

    def to_print(self, chance, j=1):
        d = ""
        if j == 1:
            for a, b in self.hand:
                d += f"\n{b} of {a}"
        else:
            d = "\n<card hidden>"
            a, b = self.hand[1]
            d += f"\n{b} of {a}"
        print(chance + d+'\n')


class Hand:
    def __init__(self):
        self.dine = []


chips = int(input("How much chips do you have? : "))


def play_again():
    print(f"Now you have {chips} chips.")
    if chips == 0:
        print("You have 0 chips.\nThanks for playing, Goodbye!")
        exit()
    j = 0
    while j == 0:
        ask = input("\nDo you want to play again? y/n : ")
        if ask[0].lower() == 'n':
            print("\tThanks for Playing, Come again soon.")
            j = 1
            exit()
        elif ask[0].lower() == 'y':
            take_bet()
            j = 1
        else:
            print("Sorry wrong input.")
            j = 0


def play():
    global chips
    lose = chips - bet
    win = chips + bet
    deck = Deck()
#    print(deck)
    player_hand = Hand()
    dealer_hand = Hand()
    pl = "The Player has :"
    dl = "The Dealer has :"
    for i in range(2):
        choose_dealer = Choose(deck, dealer_hand.dine)
    choose_dealer.to_print(dl, 2)
    for i in range(2):
        choose_player = Choose(deck, player_hand.dine)
    choose_player.to_print(pl)
    # print(choose_player.value)
    while playing:
        es = 0
        while es == 0:
            if choose_player.value > 21:
                print(f"Player Busted at {choose_player.value}, Dealer Wins!")
                print(f"\t Player's chips at {lose} ")
                chips = lose
                play_again()
            z = input("You want to hit again or stand ? h/s : ")
            if z[0].lower() == 'h':
                choose_player = Choose(deck, player_hand.dine)
                print('\n')
                choose_dealer.to_print(dl, 2)
                choose_player.to_print(pl)
                continue
            elif z[0].lower() == 's':
                print("\nDealer is playing.\n")
                while choose_dealer.value < 17:
                    choose_dealer = Choose(deck, dealer_hand.dine)
                choose_dealer.to_print(dl)
                choose_player.to_print(pl)
                if choose_dealer.value > 21:
                    print(f"Dealer Busted at {choose_dealer.value}, Player Wins!")
                    print(f"\t Player's chips at {win}")
                    chips = win
                elif choose_dealer.value < choose_player.value:
                    print("Player Wins!")
                    print(f"\t Player's chips at {win}\nPlayer Value = {choose_player.value}")
                    print(f"Dealer Value = {choose_dealer.value}")
                    chips = win
                elif choose_dealer.value > choose_player.value:
                    print("Dealer Wins!")
                    print(f"\t Player's chips at {lose}")
                    print(f"Player Value = {choose_player.value}")
                    chips = lose
                else:
                    print(f"Player Value = {choose_player.value}\nDealer Value = {choose_dealer.value}")
                    print("It's a tie, Push!")
                    print(f"\t Player's chips at {chips}")
                play_again()
                es = 1
            else:
                print("Sorry wrong input, please enter again.")


def take_bet():
    global chips
    global bet
    bet = int(input("How much you want to bet? : "))
    if bet > chips:
        print(f"Sorry you have only {chips} chips, please enter again.")
        take_bet()
    play()


take_bet()
