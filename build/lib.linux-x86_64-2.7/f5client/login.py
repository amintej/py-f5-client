import sys
from f5.bigip    import ManagementRoot

def get_login(host,user,passwd):
    try:
        mgmt = ManagementRoot(host, user, passwd,token=True)
    except Exception, e:
        print ("ERROR:Login failed for %s and user %s") %(host,user)
        sys.exit(1)
    return (mgmt)
