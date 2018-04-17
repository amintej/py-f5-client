from prettytable import PrettyTable

def get_snats(mgmt):
    snats_collection = mgmt.tm.ltm.snatpools.get_collection()
    tsnats = PrettyTable(["Partition","SNAT Pool name","SNAT Translation List","SNAT Member"])

    for snatpool in snats_collection:
        for member in snatpool.members:
            snat_translation_name=member.split("/")[2]
            snat_translation_partition=member.split("/")[1]
            snat_translation=mgmt.tm.ltm.snat_translations.snat_translation.load(name=snat_translation_name, partition=snat_translation_partition)
            tsnats.add_row([snatpool.partition,snatpool.name,member,snat_translation.address])

    tsnats.align= "l"

    return tsnats
