from mininet.topo import Topo
from mininet.util import irange

class CustomRingTopo( Topo ):
    def build(self):
        switches = [ self.addSwitch('s%s' % i ) for i in irange(1, 9)]
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1, s2, s3, s4, s5, s6, s7, s8, s9 = switches

        bw_low = 1
        bw_high = 10

        delay_low = '1ms'
        delay_high = '50ms'

        self.addLink(s1, s2, bw=bw_high, delay=delay_high)
        self.addLink(s2, s3, bw=bw_high, delay=delay_high)
        self.addLink(s3, s4, bw=bw_high, delay=delay_high)
        self.addLink(s4, s9, bw=bw_high, delay=delay_high)

        self.addLink(s1, s5, bw=bw_low, delay=delay_low)
        self.addLink(s5, s6, bw=bw_low, delay=delay_low)
        self.addLink(s6, s7, bw=bw_low, delay=delay_low)
        self.addLink(s7, s8, bw=bw_low, delay=delay_low)
        self.addLink(s8, s9, bw=bw_low, delay=delay_low)

        self.addLink(h1, s1)
        self.addLink(h2, s9)


topos = { 'custom_ring': CustomRingTopo }
