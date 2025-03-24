from models import Artifact

artifact = Artifact(
    artifact_type="Attribute",
    subtype="Water",
    main_stat="HP flat",
    sub_1="Damage Dealt on Fire +%",
    sub_2="Damage Dealt on Water +%",
    sub_3="Damage Dealt on Wind +%",
    sub_4="Damage Dealt on Light +%"
)

print(artifact)