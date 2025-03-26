from config import rune

class RuneStat:
    def __init__(self, stat_id: int, value: int, grind: int = 0):
        self.stat_id = stat_id
        self.value = value
        self.grind = grind

    def __repr__(self):
        stat = rune['stat'][self.stat_id]
        
        return (
            f"{stat} - Value : {self.value} - Grind : {self.grind}"
        )