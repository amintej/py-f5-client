from prettytable import PrettyTable
def get_partitions(mgmt):

    partitions_collection = mgmt.tm.auth.partitions.get_collection()

    tpartitions = PrettyTable(["Partition"])

    for partition in partitions_collection:
        tpartitions.add_row([partition.name])

    tpartitions.align= "l"

    return tpartitions

