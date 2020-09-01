from mininet.topo import Topo
from mininet.util import irange

class CustomCompleteBipartiteTopo( Topo ):
    def build(self):
        switches = [ self.addSwitch('s%s' % i ) for i in irange(1, 9)]
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1, s2, s3, s4, s5, s6, s7, s8, s9 = switches

        left = [s2, s3, s4, s5]
        right = [s6, s7, s8]

        bw_low = 0.1
        bw_med = 1
        bw_high = 10

        delay_low = '1ms'
        delay_med = '10ms'
        delay_high = '100ms'

        for l in left:
            for r in right:
                self.addLink(l, r, bw=bw_high, delay=delay_high)
        

        self.addLink(h1, s1)
        self.addLink(h2, s9)


topos = { 'custom_complete_bipartite': CustomCompleteBipartiteTopo }
