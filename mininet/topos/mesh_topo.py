'''
Mesh topology for Mininet

Example usage: mn --custom=mesh_topo.py --topo=mesh,3,3

For example, a 3x3 mesh looks like

s1 ----- s2 ----- s3
 | \      | \      | \
 |   h1   |   h2   |   h3
 |        |        |
s4 ----- s5 ----- s6
 | \      | \      | \
 |   h4   |   h5   |   h6
 |        |        |
s7 ----- s8 ----- s9
   \        \        \
     h7       h8       h9

'''


from mininet.topo import Topo
from mininet.util import irange

class MeshTopo( Topo ):
    def build(self, x = 3, y = 3):
        if x < 2 or y < 2:
            raise Exception('Invalid MeshTopo arguments')

        switches = [ self.addSwitch( 's%s' % ((i - 1) * y + j) ) for i in irange(1, x) for j in irange(1, y) ]
        hosts = [ self.addHost( 'h%s' % ((i - 1) * y + j) ) for i in irange(1, x) for j in irange(1, y) ]
        
        for i in range(len(switches)):
            self.addLink(hosts[i], switches[i])
        
        
        for i in range(x):
            for j in range(y - 1):
                self.addLink(switches[i * y + j], switches[i * y + j + 1])
        
        
        for i in range(x - 1):
            for j in range(y):
                self.addLink(switches[i * y + j], switches[(i + 1) * y + j])

topos = { 'mesh': MeshTopo }
