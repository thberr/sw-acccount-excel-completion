from config import rune
from models.rune_stat import RuneStat

class Rune:
    def __init__(self, set: int, stars: int, slot: int, main_stat: int, innate: int, innate_value: int, sub_stats: list[RuneStat]):
        self.set = set
        self.stars = stars
        self.slot = slot
        self.main_stat = main_stat
        self.innate = RuneStat(innate, innate_value) if innate is not None else None
        self.sub_stats = sub_stats


    def __repr__(self):
        rune_set = rune['set'][self.set]
        main_stat = rune['stat'][self.main_stat]
        innate_stat = rune['stat'][self.innate.stat_id] if self.innate else "None"
        sub_stats_str = "\n".join(
            f"{sub}" for sub in self.sub_stats
        )

        return (
            f"Set: {rune_set}\n"
            f"{self.stars}⭐\n"
            f"Slot: {self.slot}\n"
            f"Main Stat: {main_stat}\n"
            f"Innate: {innate_stat} - Value: {self.innate.value}\n"
            f"Sub Stats:\n{sub_stats_str}"
        )
    
    def from_json(json):
        # stat[2] is 1 if the stat was gemmed, or 0 if not
        sub_stats = [
            RuneStat(stat[0], stat[1], stat[3])
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