f5-client
=============

CLI for operating BIG IP systems. Available operations show, create-members, create-vs

Installation
-------------------------

1. Download wheel. Go to dist directory in the repo and downloadn wheel
2. Install pip
3. Install wheel:
  ``pip install f5_client-0.0.11-py2-none-any.whl``
4. After the installation is completed, you can use f5-client, try ``f5-client --help`` for checking available options.

Usage
-----

Use help options for displaying help and possible operations

- Show Selfs ips:
``f5-client 192.168.1.41 admin -passwd --show SE``
+-----------+------------------------+------------------------------+---------------------+
| Partition | Self IP Name           | VLAN                         | Address             |
+-----------+------------------------+------------------------------+---------------------+
| Common    | selfip_vlan100         | /Common/Lab_F5_100           | 32.150.96.243/22     |
| Common    | selfip_vlan35          | /Common/LAB_F5_Servers_Srvc2 | 192.168.33.33/27    |
| Common    | selfip_vlan35_floating | /Common/LAB_F5_Servers_Srvc2 | 192.168.33.35/27    |
| Common    | selfip_vlan36          | /Common/LAB_F5_Servers_Srvc  | 192.168.33.69/27    |
| Common    | selfip_vlan36_floating | /Common/LAB_F5_Servers_Srvc  | 192.156.33.68/27    |
| Common    | selfip_vlan37          | /Common/LAB_F5_Syn           | 1.1.1.1/29          |
+-----------+------------------------+------------------------------+---------------------+
- Check VS and SNATs:
``f5-client 192.168.1.41 admin -passwd --show SN VS``
- Create pool
``f5-client 192.168.1.1 admin -passwd --create-pool members.txt pool1 Project_387b85b4465e4a538aea77abddd347e2``
- Create VS
``f5-client 192.168.1.1 admin -passwd --create-vs pool_test3 vs-test5 10.0.10.8:85 Project_387b85b4465e4a538aea77abddd347e2 Project_387b85b4465e4a538aea77abddd347e2``

