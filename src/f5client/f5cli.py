#!/usr/bin/python

import f5.bigip
import argparse,getpass
import sys
from f5.bigip    import ManagementRoot
from prettytable import PrettyTable
from IPy import IP

def get_args():

    class Password(argparse.Action):
       def __call__(self, parser, namespace, values, option_string):
           if values is None:
               values = getpass.getpass()
           setattr(namespace, self.dest, values)


    parser = argparse.ArgumentParser(description='Script for operating bigips.',formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("host",  help="Big ip hostname")
    parser.add_argument("user",  help="Big ip user")
    parser.add_argument("-passwd",nargs='?',action=Password,help="Enter your password")
    #parser.add_argument("-passwd",help="Enter your password")
    parser.add_argument("--show",nargs="*",choices=('PA','US','VO','SE','SN','PO','VS','NO'), help="PA for showing Partitions,\nUS for showing users,\nVO for showing volumes,\nSE for showing Selfips,\nSN for showing SNATs pool,\nVS for showing Virtual Servers,\nNO for showing nodes.\nMuliple arguments allowed. Example: --show PA SE SN ")
    #parser.add_argument("--create-nodes",metavar='<filename>',help="Create nodes from a file.One node's IP per line. Example file content: \n192.168.1.1\n192.168.1.2")
    parser.add_argument("--create-pool",metavar=('<filename>','<poolname>','<partition>'),nargs=3,help="Create pool and members from a file.Example file content: \n192.168.1.1 server1.local:443\n192.168.1.2 server2.local:443")
    parser.add_argument("--create-vs",nargs=5,metavar=( '   <poolname>', '<vsname>', '<IP:Port>','<partition>','<snatpool>'),help="Create virtual server.")
    args = parser.parse_args()
    
    #print args

    host        = args.host
    user        = args.user
    passwd      = args.passwd
    showlist    = args.show
    #fnodes      = args.create_nodes
    poollist    = args.create_pool
    vslist      = args.create_vs

    return (host,user,passwd,showlist,poollist,vslist)

def main():
    from f5client import login
    from f5client import partitions
    from f5client import users
    from f5client import volumes
    from f5client import selfs
    from f5client import snats
    from f5client import nodes
    from f5client import pools
    from f5client import virtualservers


    host,user,passwd,showlist,poollist,vslist=get_args()
    mgmt=login.get_login(host,user,passwd)

    if showlist != None:
        for item in showlist:
            if item == "PA":
               tpartitions=partitions.get_partitions(mgmt)
               print tpartitions.get_string(sortby="Partition")
            elif item == "US" or item == "AL":
               tusers=users.get_users(mgmt)
               print tusers.get_string(sortby="Partition Access")
            elif item == "VO" or item == "AL":
               tvolumes=volumes.get_volumes(mgmt)
               print tvolumes.get_string(sortby="Name")
            elif item == "SE" or item == "AL":
               tselfs=selfs.get_selfs(mgmt)
               print tselfs.get_string(sortby="Partition")
            elif item == "SN":
               tsnats=snats.get_snats(mgmt)
               print tsnats.get_string(sortby="Partition")
            elif item == "PO":
               tpools=pools.get_pools(mgmt)
               print tpools.get_string(sortby="Partition")
            elif item == "NO":
               tnodes=nodes.get_nodes(mgmt)
               print tnodes.get_string(sortby="Partition")
            elif item == "VS":
               tvirtualservers=virtualservers.get_virtualservers(mgmt)
               print tvirtualservers.get_string(sortby="Partition")

    #if fnodes != None:
    #    nodes.create_nodes(mgmt,fnodes)

    if poollist != None:
       pools.create_pool(mgmt,poollist[0],poollist[1],poollist[2])

    if vslist != None:
       virtualservers.create_vs(mgmt,vslist[0],vslist[1],vslist[2],vslist[3],vslist[4])

