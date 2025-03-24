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
        return (
            f"Artifact Type: {self.artifact_type} \n" 
            f"Subtype: {self.subtype} \n"
            f"Main Stat: {self.main_stat} \n" 
            f"Sub 1: {self.sub_1} \n"
            f"Sub 2: {self.sub_2} \n"
            f"Sub 3: {self.sub_3} \n"
            f"Sub 4: {self.sub_4} \n"
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