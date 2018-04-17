from prettytable import PrettyTable

def get_selfs(mgmt):

    selfips_collection = mgmt.tm.net.selfips.get_collection()

    tselfs=PrettyTable(["Partition","Self IP Name","VLAN","Address"])

    for selfip in selfips_collection:
        tselfs.add_row([selfip.partition,selfip.name,selfip.vlan,selfip.address])

    tselfs.align= "l"

    return tselfs

