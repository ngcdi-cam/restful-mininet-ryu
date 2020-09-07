'''
Ring topology for Mininet

Example usage: mn --custom=mesh_topo.py --topo=mesh,3,3

For example, a ring topology with k=4 looks like

  h1                    h2
    \                  /
     \                /
      s1 ---------- s2
       |            |
       |            |
       |            |
       |            |
      s4 ---------- s3
     /                \
    /                  \
  h4                    h3

where k is the number of switches (and also it's the number of hosts)

'''


from mininet.topo import Topo
from mininet.util import irange

class RingTopo( Topo ):
    def build(self, k=4):
        if k < 2:
            raise Exception('k must be at least 2 for the Ring topo to work')

        switches = [ self.addSwitch( 's%s' % i ) for i in irange(1, k) ]
        hosts = [ self.addHost( 'h%s' % i) for i in irange(1, k) ]
        for i in range(k):
            self.addLink(hosts[i], switches[i])
            self.addLink(switches[i], switches[(i + 1) % k])

topos = { 'ring': RingTopo  }
