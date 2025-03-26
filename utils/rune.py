from models import RuneStat

def get_max_value_sub_stat_6(stat_id):
    match stat_id:
        case 1: return 750.0
        case 2 | 4 | 6 | 11 | 12: return 8.0
        case 3 | 5: return 40.0
        case 8 | 9: return 6.0
        case 10: return 7.0
        case _: return 0.0

def get_main_stat_max_value_5(stat_id):
    match stat_id:
        case 1: return 2088.0
        case 2: return 51.0
        case 3: return 135.0
        case 4: return 51.0
        case 5: return 135.0
        case 6: return 51.0
        case 7: return 39.0
        case 8: return 47.0
        case 9: return 65.0
        case 10: return 51.0
        case 11: return 51.0
        case _: return 0.0

def get_main_stat_max_value_6(stat_id):
    match stat_id:
        case 1: return 2448.0
        case 2: return 63.0
        case 3: return 160.0
        case 4: return 63.0
        case 5: return 160.0
        case 6: return 63.0
        case 7: return 42.0
        case 8: return 58.0
        case 9: return 80.0
        case 10: return 64.0
        case 11: return 64.0
        case _: return 0.0

def calculate_eff_stat_rune_6(stat: RuneStat):
    stat_max_value = get_max_value_sub_stat_6(stat.stat_id)
    stat_total_value = stat.value + stat.grind
    
    return stat_total_value / (stat_max_value * 5.0)