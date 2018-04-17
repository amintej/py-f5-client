import sys
from prettytable import PrettyTable

def get_nodes(mgmt):

    nodes_collection = mgmt.tm.ltm.nodes.get_collection()
    tnodes = PrettyTable(["Partition","Node Name","Node administrative state","Node state","Monitor","Monitor state"])

    for node in nodes_collection:
        tnodes.add_row([node.partition,node.name,node.session,node.state,node.monitor,node.state])

    tnodes.align= "l"

    return tnodes

def create_nodes(mgmt,f):
    try:
        nodes = open(f).read().splitlines()
    except IOError as err:
        print ("ERROR: File %s not found" % f)
        sys.exit(1)
    try:
        for node in nodes:
            print node
            IP(node)
    except ValueError as err:
        print ("ERROR:Invalid IP %s. It can't be imported" % node)
        sys.exit(1)

    try:
        for node in nodes:
            if mgmt.tm.ltm.nodes.node.exists(name=node,partition='Common') == False:
                node = mgmt.tm.ltm.nodes.node.create(name=node, address=node, description='Added by f5-client', partition='Common')
                print ("New node created %s" % node.name)
            else:
                print ("Node already exists %s" % node)
    except Exception,e:
        print e
        sys.exit(1)

