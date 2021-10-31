class ATM(object):
    def __init__(self,name, paiseOthao, prank):
        self.name=name
        self.paiseOthao=paiseOthao
        self.prank=prank
    
    def ruppeOthao(self,cash):
        print(cash,"WithDrawed")
    
    def looted(self):
        print("you are looted:) have a nice day")
louis=ATM("Louis XVI",300,600)
louis.ruppeOthao(200)
louis.looted()