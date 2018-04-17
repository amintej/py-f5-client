import sys
from prettytable import PrettyTable

def get_pools(mgmt):

    pools = mgmt.tm.ltm.pools.get_collection()
    tpools = PrettyTable(["Partition","Pool Name","Member","Member IP","Op state","Monitor"])

    for pool in pools:
        for member in pool.members_s.get_collection():
            pool_stats=pool.stats.load()
            tpools.add_row ([pool.partition,pool.name,member.name,member.address,member.state,pool.monitor])

    tpools.align= "l"

    return tpools

def create_pool(mgmt,f,p_name,pa_name):
    try:
        poolmembers = open(f).read().splitlines()
    except IOError as err:
        print ("ERROR: File %s not found" % f)
        sys.exit(1)

    try:
        if mgmt.tm.ltm.pools.pool.exists(name=p_name,partition=pa_name) == True:
            print ("ERROR:Pool %s already exists" % p_name)
            sys.exit(1)
        else:
            pool1 = mgmt.tm.ltm.pools.pool.create(name=p_name,partition=pa_name,monitor='tcp',description='Added by f5-client')
            members = pool1.members_s
            member  = pool1.members_s.members
            for m in poolmembers:
                pool1.members_s.members.create(name=m.split(" ")[1],address=m.split(" ")[0],partition=pa_name)
                print ("New member added %s" % m)
    except Exception,e:
        print e

