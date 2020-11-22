from random import shuffle
class Card:
    suits = ["スペード", "ハート", "ダイア", "クラブ"]

    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

            
    def __init__(self, v, s): #カードの数値とマークを与える
        #マークもあたいも整数値
        self.value = v
        self.suit = s

    def __lt__(self, c2): #カードの強さを比べる (<)を使う時に呼びだす
        if self.value < c2.value:
            return True

        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2): #カードの強さを比べる(>)を使う時に呼び出す
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.value > c2.value:
                return True
            else:
                return False

        return False

    def __repr__(self): #カードのマークと値を出力
        v = self.suits[self.suit] + "の" \
            + self.values[self.value]
        return v

class Deck:
    def __init__(self): #トランプの並びを決定
        self.cards = []
        #self.cardsに52通りの数を代入しシャッフル
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self): #cardsリストから要素を1つ選び、削除しその要素を返す。リストが空だったらNoneを返す。
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name): #プレーヤーの勝ち数、カード、名前をあたえる
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self): #プレーヤーの名前をinput,「Deck」メソッドでデッキを決定,
        name1 = input("プレーヤー1の名前")
        name2 = input("プレーヤー2の名前")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins (self, winner): #１ターンの勝者を出力
        w = "こののラウンドは {} が勝ちました"
        w = w.format(winner)
        print(w)
    
    def draw(self, p1n, p1c, p2n, p2c): #プレーヤーが引いたカードを「__repr__」メソッドを用いて出力
        d = "{} は {} 、 {} は {} を引きました"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self): #ゲームの開始
        cards = self.deck.cards
        print("戦争を始めます")
        #cardsリストが2以上のとき実行、qが入力されるか、cardsリストが2未満のとき終了
        while len(cards) >= 2 :
            m = "qで終了、それ以外のキーでplay"
            response = input(m)
            if response == 'q':
                break
            #p1c、p2cはプレーヤー1、プレーヤー2がそれぞれ引いたカード
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            #p1n、p2nはそれぞれプレーヤー1、プレーヤー2の名前
            p1n = self.p1.name
            p2n = self.p2.name
            #drawメソッドの実行
            self.draw(p1n, p1c, p2n, p2c)
            
            if p1c > p2c: #「__gt__」メソッドを使用しTrueのときプレーヤ1の勝ち数を+1
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:#ifがTrue以外の時プレーヤー2の勝ち数を+1
                self.p2.wins += 1
                self.wins(self.p2.name)
        #winnerメソッドの実行    
        win = self.winner(self.p1, self.p2)
        print("ゲームの終了、{} です！".format(win))

    def winner(self, p1, p2): #プレーヤー1の勝ち数とプレーヤー2の勝ち数を比べ結果によって、ゲームの勝敗を出力
        if p1.wins > p2.wins: 
            return "{} の勝利".format(p1.name)
        if p1.wins < p2.wins:
            return "{} の勝利".format(p2.name)
        return "引き分け"

game = Game()
game.play_game()