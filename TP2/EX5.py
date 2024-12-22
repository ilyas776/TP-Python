class animal:
    def faire_du_bruit():
        pass
class chat(animal):
    def faire_du_bruit(self):
        print("chat")

class chien(animal):
    def faire_du_bruit(self):
        print("chien")

chat1=chat()
chien1=chien()
chat1.faire_du_bruit()
chien1.faire_du_bruit()

