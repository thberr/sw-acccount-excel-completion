from config import artifact

class Artifact:
    def __init__(self, artifact_type, subtype, main_stat, sub_1, sub_2, sub_3, sub_4):
        self.artifact_type = artifact_type
        self.subtype = subtype
        self.main_stat = main_stat
        self.sub_1 = sub_1
        self.sub_2 = sub_2
        self.sub_3 = sub_3
        self.sub_4 = sub_4

    def __repr__(self):
        artifact_type = artifact['type'][self.artifact_type]
        subtype = artifact['attribute'][self.subtype] if self.artifact_type == 1 else artifact['archetype'][self.subtype]
        main_stat = artifact['main'][self.main_stat]
        sub_1 = artifact['sub'][self.sub_1[0]]
        sub_1_value = self.sub_1[1]
        sub_2 = artifact['sub'][self.sub_2[0]]
        sub_2_value = self.sub_2[1]
        sub_3 = artifact['sub'][self.sub_3[0]]
        sub_3_value = self.sub_3[1]
        sub_4 = artifact['sub'][self.sub_4[0]]
        sub_4_value = self.sub_4[1]
        
        return (
            f"Artifact Type: {artifact_type} \n"
            f"Subtype: {subtype} \n"
            f"Main Stat: {main_stat} \n"
            f"Sub 1: {sub_1} : {sub_1_value}% \n"
            f"Sub 2: {sub_2} : {sub_2_value}% \n"
            f"Sub 3: {sub_3} : {sub_3_value}% \n"
            f"Sub 4: {sub_4} : {sub_4_value}% \n"
        )

    def from_json(json):
        return Artifact(
            artifact_type=json["type"],
            subtype=json["attribute"] if json["type"] == 1 else json["unit_style"],
            main_stat=json["pri_effect"][0],
            sub_1=json["sec_effects"][0],
            sub_2=json["sec_effects"][1],
            sub_3=json["sec_effects"][2],
            sub_4=json["sec_effects"][3],
        )