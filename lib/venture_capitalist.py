from .funding_round import FundingRound

class VentureCapitalist:

    all = []
    
    def __init__(self, name, total_worth):
        if type(name) == str:
            self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

    @classmethod
    def tres_commas_club(cls):
        return [ vc for vc in cls.all if vc.total_worth >1000000000]
