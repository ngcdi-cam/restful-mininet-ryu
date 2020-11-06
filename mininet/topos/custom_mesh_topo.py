from mininet.topo import Topo
from mininet.util import irange

class CustomMeshTopo( Topo ):
    def build(self):
        switches = [ self.addSwitch('s%s' % i ) for i in irange(1, 25)]
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        # h3 = self.addHost('h3')
        # h4 = self.addHost('h4')
        # h5 = self.addHost('h5')

        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25 = switches

        bw_low = 0.1
        bw_med = 1
        bw_high = 10

        delay_low = '1ms'
        delay_med = '50ms'
        delay_high = '100ms'
        delay_xhigh = '200ms'

        self.addLink(s1, s6, bw=bw_med, delay=delay_low)
        self.addLink(s1, s2, bw=bw_high, delay=delay_high) #
        self.addLink(s2, s7, bw=bw_med, delay=delay_high)
        self.addLink(s2, s3, bw=bw_high, delay=delay_high)
        self.addLink(s3, s8, bw=bw_med, delay=delay_med)
        self.addLink(s3, s4, bw=bw_high, delay=delay_high)
        self.addLink(s4, s9, bw=bw_low, delay=delay_low)
        self.addLink(s4, s5, bw=bw_high, delay=delay_high)

        self.addLink(s5, s10, bw=bw_high, delay=delay_high)
        self.addLink(s6, s11, bw=bw_med, delay=delay_low)
        self.addLink(s6, s7, bw=bw_med, delay=delay_med)
        self.addLink(s7, s12, bw=bw_low, delay=delay_low)
        self.addLink(s7, s8, bw=bw_med, delay=delay_high)
        self.addLink(s8, s13, bw=bw_med, delay=delay_high)
        self.addLink(s8, s9, bw=bw_low, delay=delay_med)
        self.addLink(s9, s14, bw=bw_low, delay=delay_high)
        self.addLink(s9, s10, bw=bw_med, delay=delay_low)
        self.addLink(s10, s15, bw=bw_high, delay=delay_high)
        self.addLink(s11, s16, bw=bw_med, delay=delay_low)
        self.addLink(s11, s12, bw=bw_high, delay=delay_med)
        self.addLink(s12, s17, bw=bw_med, delay=delay_med)
        self.addLink(s12, s13, bw=bw_med, delay=delay_high)
        self.addLink(s13, s18, bw=bw_med, delay=delay_high)
        self.addLink(s13, s14, bw=bw_low, delay=delay_high)
        self.addLink(s14, s19, bw=bw_low, delay=delay_med)
        self.addLink(s14, s15, bw=bw_high, delay=delay_low)
        self.addLink(s15, s20, bw=bw_high, delay=delay_high)
        self.addLink(s16, s21, bw=bw_med, delay=delay_low)
        self.addLink(s16, s17, bw=bw_low, delay=delay_med)
        self.addLink(s17, s22, bw=bw_low, delay=delay_med)
        self.addLink(s17, s18, bw=bw_high, delay=delay_med)
        self.addLink(s18, s23, bw=bw_high, delay=delay_low)
        self.addLink(s18, s19, bw=bw_high, delay=delay_high)
        self.addLink(s19, s24, bw=bw_high, delay=delay_low)
        self.addLink(s19, s20, bw=bw_low, delay=delay_low)
        self.addLink(s20, s25, bw=bw_high, delay=delay_high)
        self.addLink(s21, s22, bw=bw_med, delay=delay_low)
        self.addLink(s22, s23, bw=bw_med, delay=delay_low)
        self.addLink(s23, s24, bw=bw_med, delay=delay_low)
        self.addLink(s24, s25, bw=bw_med, delay=delay_low)


        #self.addLink(s6, s5, bw=bw_low, delay=delay_xhigh)

        self.addLink(h1, s1)
        self.addLink(h2, s25)

        # self.addLink(h3, s3)
        # self.addLink(h4, s7)
        #
        # self.addLink(h5, s9)



topos = { 'custom_mesh': CustomMeshTopo }
