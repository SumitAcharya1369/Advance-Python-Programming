class studentidcard:
    def issue_card(self):
        print("student id card issued")

class facultyidcard:
    def issue_card(self):
        print("faculty id card is issued")


class staffidcard:
    def issue_card(self):
        print("staff id card issued")


class id_card_factory:

    def get_card(self,card_type):

        if card_type=="student":
            return studentidcard()
        
        elif card_type =="factory":
            return facultyidcard()
        
        elif card_type =="staff":
            return staffidcard()
        
        else:
            print("invalid card type")
            return None
        
factory = id_card_factory()
card = factory.get_card("student")
card.issue_card()


card= factory.get_card("factory")
card.issue_card()


card=factory.get_card("staff")
card.issue_card()