from config import rune
from models.rune_stat import RuneStat
from utils.rune import get_main_stat_max_value_6, calculate_eff_stat_rune_6

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
    
    def calculate_rune_efficiency(self) -> float:
        eff_main = get_main_stat_max_value_6(self.main_stat)/get_main_stat_max_value_6(self.main_stat)
        eff_innate = 0.0
        eff_subs = 0.0

        if self.innate:
            eff_innate = calculate_eff_stat_rune_6(self.innate)
        for stat in self.sub_stats:
            eff_subs += calculate_eff_stat_rune_6(stat)

        return round(((eff_main + eff_innate + eff_subs) / 2.8) * 100.0, 2)