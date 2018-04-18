from prettytable import PrettyTable
def get_users(mgmt):
    
    users_collection = mgmt.tm.auth.users.get_collection()

    tusers = PrettyTable(["Username","Partition Access","Role"])

    for user in users_collection:
        user_role=user.partitionAccess[0]['role']
        user_partition=user.partitionAccess[0]['name']
        tusers.add_row([user.name,user_partition,user_role])

    tusers.align = "l"

    return tusers


