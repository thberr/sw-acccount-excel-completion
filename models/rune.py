from config import rune
from models.rune_stat import RuneStat

class Rune:
    def __init__(self, set, stars, slot, main_stat, innate, innate_value, sub_stats):
        self.set = set
        self.stars = stars
        self.slot = slot
        self.main_stat = main_stat
        self.innate = {'stat': innate, 'value': innate_value}
        self.subs = [RuneStat(sub['stat'], sub['value'], sub['grind']) for sub in sub_stats]


    def __repr__(self):
        rune_set = rune['set'][self.set]
        main_stat = rune['stat'][self.main_stat]
        innate_stat = rune['stat'][self.innate['stat']] if self.innate['stat'] else "None"
        sub_stats_str = "\n".join(
            f"{sub}" for sub in self.subs
        )

        return (
            f"Set: {rune_set}\n"
            f"{self.stars}⭐\n"
            f"Slot: {self.slot}\n"
            f"Main Stat: {main_stat}\n"
            f"Innate: {innate_stat} - Value: {self.innate['value']}\n"
            f"Sub Stats:\n{sub_stats_str}"
        )
    
    def from_json(json):
        # stat[2] is 1 if the stat was gemmed, or 0 if not
        sub_stats = [
            {'stat': stat[0], 'value': stat[1], 'grind': stat[3]}
            for stat in json.get('sec_eff', [])
        ]

        return Rune(
            set=json['set_id'],
            stars=json['class'],
            slot=json['slot_no'],
            main_stat=json['pri_eff'][0],
            innate=json["prefix_eff"][0] if json.get("prefix_eff") and json["prefix_eff"][0] != 0 else None,
            innate_value=json["prefix_eff"][1] if json.get("prefix_eff") and json["prefix_eff"][0] != 0 else None,
            sub_stats=sub_stats,
        )