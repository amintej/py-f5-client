from prettytable import PrettyTable
def get_volumes(mgmt):

    volumes_collection = mgmt.tm.sys.software.volumes.get_collection()

    tvolumes = PrettyTable(["Name","Version","Build","Active"])

    for volume in volumes_collection:
        
        if hasattr(volume,'version') == False:
            tvolumes.add_row([volume.name,"N/A","N/A", "False"])
        elif hasattr(volume,'active') == False:
            tvolumes.add_row([volume.name,volume.version,volume.build, "False"])
        else:
            tvolumes.add_row([volume.name,volume.version,volume.build, volume.active])

    tvolumes.align = "l"

    return tvolumes
