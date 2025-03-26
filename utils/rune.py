from models.rune_stat import RuneStat

def get_max_value_sub_stat_6(stat_id) -> int:
    match stat_id:
        case 1: return 750
        case 2 | 4 | 6 | 11 | 12: return 8
        case 3 | 5: return 40
        case 8 | 9: return 6
        case 10: return 7
        case _: return 0

def get_main_stat_max_value_5(stat_id) -> int:
    match stat_id:
        case 1: return 2088
        case 2: return 51
        case 3: return 135
        case 4: return 51
        case 5: return 135
        case 6: return 51
        case 7: return 39
        case 8: return 47
        case 9: return 65
        case 10: return 51
        case 11: return 51
        case _: return 0

def get_main_stat_max_value_6(stat_id) -> int:
    match stat_id:
        case 1: return 2448
        case 2: return 63
        case 3: return 160
        case 4: return 63
        case 5: return 160
        case 6: return 63
        case 7: return 42
        case 8: return 58
        case 9: return 80
        case 10: return 64
        case 11: return 64
        case _: return 0

def calculate_eff_stat_rune_6(stat: RuneStat) -> float:
    stat_max_value = get_max_value_sub_stat_6(stat.stat_id)
    stat_total_value = stat.value + stat.grind
    
    return stat_total_value / (stat_max_value * 5)