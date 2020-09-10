#!/usr/bin/python3

from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.topo import LinearTopo
from mininet.topo import SingleSwitchTopo
from mininet.topolib import TreeTopo
from functools import partial
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

from mininet_rest import MininetRest
from topos.custom_mesh_topo import CustomMeshTopo

import threading

# c1 = RemoteController('c1', ip='awareness1', port=6633)
# c2 = RemoteController('c2', ip='awareness2', port=6633)

c1 = RemoteController('c1', ip='127.0.0.1', port=6653)
c2 = RemoteController('c2', ip='127.0.0.1', port=6654)

cmap = {'s1': c1, 's2': c2, 's3': c2, 's4': c1,
        's5': c1, 's6': c2, 's7': c1, 's8': c1, 's9': c2}

def start_mininet_rest(net):
    MininetRest(net).run(host='0.0.0.0', port=8888)

class MultiSwitch(OVSSwitch):
    "Custom Switch() subclass that connects to different controllers"

    def start(self, controllers):
        return OVSSwitch.start(self, [cmap[self.name]])

net = Mininet(topo=CustomMeshTopo(), cleanup=True, link=TCLink, switch=MultiSwitch, controller=None)

net.start()
threading.Thread(target=start_mininet_rest, args=(net,)).start()
CLI(net)
net.stop()

