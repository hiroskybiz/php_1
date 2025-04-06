class Player:
    __charactor_count = 0
    @classmethod
    def summary(cls):
        print(str(Player.__charactor_count)+"�l�ŁA�G���m���U�������B") 
        
    def __init__(self, name):
        self.name = name
        Player.__charactor_count += 1
        print(str(Player.__charactor_count)+"�Ԗڂ̃v���[���["+self.name + "���o�ꂵ���B")

    def attack(self, enemy):
        print(self.name + "�́A" + enemy + "���U�������I")
        
    #summary = classmethod(summary)

class Wizard(Player):
    def __init__(self):
        super().__init__("�S�C���m")

    def attack(self, enemy):
        self.__spell()
        print(self.name + "�́A" + enemy + "�ɓS�C��������I")

    def __spell(self):
        print("�Y�o�[���I")

print("=== �R�c�œG�R�Ɛ키 ===")
hero = Player("�퍑����")
warrior = Player("�������m")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("�G��")
    
Player.summary()
