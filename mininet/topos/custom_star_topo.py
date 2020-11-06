from mininet.topo import Topo
from mininet.util import irange

class CustomStarTopo( Topo ):
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

        self.addLink(s1, s2, bw=bw_low, delay=delay_med)

        self.addLink(s1, s3, bw=bw_high, delay=delay_low)

        self.addLink(s1, s4, bw=bw_high, delay=delay_low)

        self.addLink(s1, s5, bw=bw_high, delay=delay_high)

        self.addLink(s1, s6, bw=bw_low, delay=delay_med)

        self.addLink(s1, s7, bw=bw_high, delay=delay_low)

        self.addLink(s1, s8, bw=bw_high, delay=delay_med)

        self.addLink(s1, s9, bw=bw_low, delay=delay_high)

        self.addLink(s1, s10, bw=bw_low, delay=delay_med)

        self.addLink(s1, s11, bw=bw_med, delay=delay_med)

        self.addLink(s1, s12, bw=bw_med, delay=delay_high)

        self.addLink(s1, s13, bw=bw_low, delay=delay_low)

        self.addLink(s1, s14, bw=bw_high, delay=delay_med)

        self.addLink(s1, s15, bw=bw_high, delay=delay_low)

        self.addLink(s1, s16, bw=bw_low, delay=delay_high)

        self.addLink(s1, s17, bw=bw_med, delay=delay_med)

        self.addLink(s1, s18, bw=bw_med, delay=delay_high)

        self.addLink(s1, s19, bw=bw_med, delay=delay_high)

        self.addLink(s1, s20, bw=bw_med, delay=delay_high)

        self.addLink(s1, s21, bw=bw_low, delay=delay_low)

        self.addLink(s1, s22, bw=bw_med, delay=delay_med)

        self.addLink(s1, s23, bw=bw_high, delay=delay_low)

        self.addLink(s1, s24, bw=bw_high, delay=delay_low)

        self.addLink(s1, s25, bw=bw_med, delay=delay_low)

        self.addLink(s1, s26, bw=bw_med, delay=delay_low)

        self.addLink(h1, s1)
        self.addLink(h2, s9)


topos = { 'custom_star': CustomStarTopo }
