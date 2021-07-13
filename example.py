#所蔵本リスト
class BookList():
    def __init__(self):
        self.BOOKS = {"昆虫図鑑":"A-3","怪獣図鑑":"B-2","植物図鑑":"C-1","鉱物図鑑":"D-4"}

    def searchBook(self,bookName):
        #本の名前から探す
        #あればその場所を、なければNoneを返す
        if bookName in self.BOOKS:
            location = self.BOOKS[bookName]
        else:
            location = None

        return location

#貸出帳
class LendingList():
    def __init__(self):
        self.BOOKS = ["怪獣図鑑","鉱物図鑑"]
    
    def check(self, bookName):
        #貸出帳をチェックする
        #貸出中ならtrue,そうでなければfalseを返す
        if bookName in self.BOOKS:
            return True
        else:
            return False

#図書委員の中村くん
class Librarian():
    def searchBook(self,bookName):
        #本を探す
        bookList = BookList()
        location = bookList.searchBook(bookName)

        #本の場所がNoneではない（所蔵してる）とき
        if location is not None:
            #貸出中かチェックする
            lendingList = LendingList()
            if lendingList.check(bookName):
                #貸出中のとき
                return "貸出中です"
            else:
                return location
        #所蔵してないとき
        else:
            return "その本は所蔵していません"

class Visitor():
    def __init__(self,bookName):
        self.bookName = bookName

    def reaction(self):
        #窓口の中村くんを作る
        nakamura = Librarian()
        #中村くんに本の場所を聞く
        location = nakamura.searchBook(self.bookName)
        if location == "貸出中です":
            return "貸出中かよ・・・"
        elif location == "その本は所蔵していません":
            return "なんだ、ないのか"
        else:
            return location + "ね。分かった、サンキュ！"

if __name__=='__main__':
    yamada = Visitor("昆虫図鑑")
    print(yamada.reaction())

    tanaka = Visitor("鉱物図鑑")
    print(tanaka.reaction())

    sudou = Visitor("惑星図鑑")
    print(sudou.reaction())