import sys
from prettytable import PrettyTable

def get_virtualservers(mgmt):

    virtualservers_collection = mgmt.tm.ltm.virtuals.get_collection()
    tvirtualservers = PrettyTable(["Partition","VS Name","VS Description","IP","Port","Pool","SNAT Pool"])

    for virtualserver in virtualservers_collection:
        virtual_port=virtualserver.destination.split(":")[1]
        virtual_address_name=virtualserver.destination.split("/")[2].split(":")[0]
        virtual_address=mgmt.tm.ltm.virtual_address_s.virtual_address.load(name=virtual_address_name, partition=virtualserver.partition)
        
        if hasattr (virtualserver, 'description') == False:
            virtualserver.description = " "

        if virtualserver.sourceAddressTranslation['type'] == "snat" and virtualserver.sourceAddressTranslation['pool'].find("/") != -1:
            virtual_snat=virtualserver.sourceAddressTranslation['pool'].split("/")[2]
       
        if virtualserver.sourceAddressTranslation['type'] == "none" or virtualserver.sourceAddressTranslation['type'] == "automap":
            virtual_snat=virtualserver.sourceAddressTranslation['type']

        #virtual_address=mgmt.tm.ltm.virtual_address_s.virtual_address.load(name=virtual_address_name, partition=virtualserver.partition)

        if hasattr (virtualserver, 'pool') and virtualserver.pool.find("/") != -1:
            virtual_poolname=virtualserver.pool.split("/")[2]
            tvirtualservers.add_row ([virtualserver.partition,virtualserver.name,virtualserver.description,virtual_address.address,virtual_port,virtual_poolname,virtual_snat])
        else: 
            tvirtualservers.add_row ([virtualserver.partition,virtualserver.name,virtualserver.description,virtual_address.address,virtual_port,'Not defined',virtual_snat])

    tvirtualservers.align = "l"

    return tvirtualservers

def create_vs(mgmt,p_name,vs_name,vs_destination,pa_name,snatpool):
    try:
        if mgmt.tm.ltm.pools.pool.exists(name=p_name,partition=pa_name) == False:
           print ("Pool %s doesn't exist. Please create first." % p_name)
           sys.exit(1)
        elif mgmt.tm.ltm.virtuals.virtual.exists(name=vs_name,partition=pa_name) == True:
           print ("VS %s already exists" % vs_name)
           sys.exit(1)
        elif mgmt.tm.ltm.virtuals.virtual.create(name=vs_name,destination=vs_destination,ipProtocol='tcp',pool=p_name,description='Added by f5-client',partition=pa_name):
           print ("New VS created %s %s" % (vs_name,vs_destination))
           vipa=mgmt.tm.ltm.virtuals.virtual.load(name=vs_name,partition=pa_name)
           vipa.sourceAddressTranslation = {"type" : "snat", "pool" : snatpool }
           vipa.update()   
    except Exception, e:
        print e
        sys.exit(1)
