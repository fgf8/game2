class Card:
    suits=["spades", "hearts", "diamonds", "clubs"]

    values=[None, None, "2", "3", "4", "5", "6", "7", "8", "9",
            "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value=v
        self.suit=s

    def __lt__(self, c2):
        if self.value<c2.value:
            return True
        if self.value==c2.value:
            if self.suit<c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value>c2.value:
            return True
        if self.value==c2.value:
            if self.suit>c2.value:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v=self.values[self.value] + " of "\
           +self.suits[self.suit]
        return v





from random import shuffle

class Deck:
    def __init__(self):
        self.cards=[]
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()



class Player:
    def __init__(self, name):
        self.wins=0
        self.card=None
        self.name=name



class Game:
    def __init__(self):
        name1=input("プレイヤー１の名前：")
        name2=input("プレイヤー２の名前：")
        self.deck=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)

    def wins(self, winner):
        w="このラウンドは{}が勝ちました"
        w=w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d="{}は{}、{}は{}を引きました"
        d=d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards=self.deck.cards
        print("ゲームを始めます")
        while len(cards)>=2:
            m="qで終了、それ以外のキーでPlay:"
            response=input(m)
            if response=="q":
                break
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)

        win=self.winner(self.p1, self.p2)
        print("ゲーム終了、{}の勝利です".format(win))

    def winner(self, p1, p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins<p2.wins:
            return p2.name
        return "引き分け"




ython 3.10.1 (v3.10.1:2cd268a3a9, Dec  6 2021, 14:28:59) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class Card:
    suits=["spades", "hearts", "diamonds", "clubs"]

    values=[None, None, "2", "3", "4", "5", "6", "7", "8", "9",
            "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value=v
        self.suit=s

    def __lt__(self, c2):
        if self.value<c2.value:
            return True
        if self.value==c2.value:
            if self.suit<c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value>c2.value:
            return True
        if self.value==c2.value:
            if self.suit>c2.value:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v=self.values[self.value] + " of "\
           +self.suits[self.suit]
        return v

    
card=Card(3, 2)
print(card)
3 of diamonds


l=list(range(10))
print(l)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l.pop(2))
2
print(l)
[0, 1, 3, 4, 5, 6, 7, 8, 9]

================================ RESTART: Shell ================================
from radom import shuffle
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    from radom import shuffle
ModuleNotFoundError: No module named 'radom'


================================ RESTART: Shell ================================
from random import shuffle
class Card:
    suits=["spades", "hearts", "diamonds", "clubs"]

    values=[None, None, "2", "3", "4", "5", "6", "7", "8", "9",
            "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value=v
        self.suit=s

    def __lt__(self, c2):
        if self.value<c2.value:
            return True
        if self.value==c2.value:
            if self.suit<c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value>c2.value:
            return True
        if self.value==c2.value:
            if self.suit>c2.value:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v=self.values[self.value] + " of "\
           +self.suits[self.suit]
        return v

    
class Deck:
    def __init__(self):
        self.cards=[]
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, J))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()

    
deck=Deck()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    deck=Deck()
  File "<pyshell#14>", line 6, in __init__
    self.cards.append(Card(i, J))
NameError: name 'J' is not defined. Did you mean: 'j'?
f
class Deck:
    def __init__(self):
        self.cards=[]
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()

    
deck=Deck()
for card in deck.cards:
    print(card)

    
Jack of clubs
9 of spades
6 of clubs
3 of diamonds
7 of diamonds
3 of clubs
Ace of spades
7 of spades
2 of diamonds
5 of diamonds
King of diamonds
Queen of spades
5 of clubs
Ace of diamonds
King of spades
10 of spades
2 of hearts
6 of spades
10 of clubs
8 of diamonds
King of clubs
5 of hearts
Jack of diamonds
Ace of hearts
8 of hearts
Jack of spades
Queen of diamonds
King of hearts
Ace of clubs
6 of diamonds
2 of spades
5 of spades
4 of diamonds
8 of clubs
4 of spades
6 of hearts
Queen of clubs
Jack of hearts
2 of clubs
9 of diamonds
9 of hearts
3 of spades
10 of hearts
10 of diamonds
8 of spades
9 of clubs
4 of hearts
3 of hearts
7 of hearts
4 of clubs
Queen of hearts
7 of clubs

================================ RESTART: Shell ================================
from random import shuffle
class Card:
    suits=["spades", "hearts", "diamonds", "clubs"]

    values=[None, None, "2", "3", "4", "5", "6", "7", "8", "9",
            "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value=v
        self.suit=s

    def __lt__(self, c2):
        if self.value<c2.value:
            return True
        if self.value==c2.value:
            if self.suit<c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value>c2.value:
            return True
        if self.value==c2.value:
            if self.suit>c2.value:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v=self.values[self.value] + " of "\
           +self.suits[self.suit]
        return v

    
class Deck:
    def __init__(self):
        self.cards=[]
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()

    
class Player:
    def __init__(self, name):
        self.wins=0
        self.card=None
        self.name=name


class Game:
    def __init__(self):
        name1=input("プレイヤー１の名前：")
        name2=input("プレイヤー２の名前：")
        self.deck=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)

    def wins(self, winner):
        w="このラウンドは{}が勝ちました"
        w=w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d="{}は{}、{}は{}を引きました"
        d=d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards=self.deck.cards
        print("ゲームを始めます")
        while len(cards)>=2:
            m="qで終了、それ以外のキーでPlay:"
            response=input(m)
            if response=="q":
                break
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)

        win=self.winner(self.p1, self.p2)
        print("ゲーム終了、{}の勝利です".format(win))

    def winner(self, p1, p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins<p2.wins:
            returen p2.name
        return "引き分け"

    
SyntaxError: invalid syntax
class Game:
    def __init__(self):
        name1=input("プレイヤー１の名前：")
        name2=input("プレイヤー２の名前：")
        self.deck=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)

    def wins(self, winner):
        w="このラウンドは{}が勝ちました"
        w=w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d="{}は{}、{}は{}を引きました"
        d=d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards=self.deck.cards
        print("ゲームを始めます")
        while len(cards)>=2:
            m="qで終了、それ以外のキーでPlay:"
            response=input(m)
            if response=="q":
                break
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)

        win=self.winner(self.p1, self.p2)
        print("ゲーム終了、{}の勝利です".format(win))

    def winner(self, p1, p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins<p2.wins:
            return p2.name
        return "引き分け"

    

game=Game()
プレイヤー１の名前：かない
プレイヤー２の名前：いくた
game.play_game()
ゲームを始めます
qで終了、それ以外のキーでPlay:o
かないは3 of diamonds、いくたはAce of spadesを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないはQueen of spades、いくたはKing of spadesを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないは5 of diamonds、いくたは9 of clubsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないは6 of hearts、いくたは7 of spadesを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないは6 of spades、いくたはQueen of clubsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないは2 of diamonds、いくたは2 of heartsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないはAce of clubs、いくたは4 of heartsを引きました
このラウンドはかないが勝ちました
qで終了、それ以外のキーでPlay:]
かないは2 of spades、いくたは7 of diamondsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないはJack of spades、いくたは8 of heartsを引きました
このラウンドはかないが勝ちました
qで終了、それ以外のキーでPlay:]
かないは9 of diamonds、いくたは10 of clubsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないは4 of spades、いくたはJack of diamondsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないは10 of spades、いくたは2 of clubsを引きました
このラウンドはかないが勝ちました
qで終了、それ以外のキーでPlay:]
かないはQueen of diamonds、いくたは7 of heartsを引きました
このラウンドはかないが勝ちました
qで終了、それ以外のキーでPlay:]
かないはQueen of hearts、いくたはJack of clubsを引きました
このラウンドはかないが勝ちました
qで終了、それ以外のキーでPlay:]
かないは3 of clubs、いくたはKing of heartsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないは9 of spades、いくたは6 of clubsを引きました
このラウンドはかないが勝ちました
qで終了、それ以外のキーでPlay:]
かないはKing of clubs、いくたは9 of heartsを引きました
このラウンドはかないが勝ちました
qで終了、それ以外のキーでPlay:]
かないは5 of spades、いくたは10 of heartsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないは8 of diamonds、いくたは8 of clubsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないは3 of spades、いくたは6 of diamondsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないは3 of hearts、いくたはKing of diamondsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないはAce of diamonds、いくたは10 of diamondsを引きました
このラウンドはかないが勝ちました
qで終了、それ以外のキーでPlay:]
かないはJack of hearts、いくたは4 of diamondsを引きました
このラウンドはかないが勝ちました
qで終了、それ以外のキーでPlay:]
かないは8 of spades、いくたは5 of heartsを引きました
このラウンドはかないが勝ちました
qで終了、それ以外のキーでPlay:]
かないは5 of clubs、いくたは7 of clubsを引きました
このラウンドはいくたが勝ちました
qで終了、それ以外のキーでPlay:]
かないはAce of hearts、いくたは4 of clubsを引きました
このラウンドはかないが勝ちました
ゲーム終了、いくたの勝利です
]
SyntaxError: unmatched ']'
