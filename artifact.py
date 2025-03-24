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