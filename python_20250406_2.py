class Player:
    __charactor_count = 0
    @classmethod
    def summary(cls):
        print(str(Player.__charactor_count)+"l‚ÅA“G•ºm‚ğUŒ‚‚µ‚½B") 
        
    def __init__(self, name):
        self.name = name
        Player.__charactor_count += 1
        print(str(Player.__charactor_count)+"”Ô–Ú‚ÌƒvƒŒ[ƒ„["+self.name + "‚ª“oê‚µ‚½B")

    def attack(self, enemy):
        print(self.name + "‚ÍA" + enemy + "‚ğUŒ‚‚µ‚½I")
        
    #summary = classmethod(summary)

class Wizard(Player):
    def __init__(self):
        super().__init__("“S–C•ºm")

    def attack(self, enemy):
        self.__spell()
        print(self.name + "‚ÍA" + enemy + "‚É“S–C‚ğ•ú‚Á‚½I")

    def __spell(self):
        print("ƒYƒo[ƒ“I")

print("=== ŒR’c‚Å“GŒR‚Æí‚¤ ===")
hero = Player("í‘•Ò")
warrior = Player("’·‘„•ºm")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("“G•º")
    
Player.summary()
