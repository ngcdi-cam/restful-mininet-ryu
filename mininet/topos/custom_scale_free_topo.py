from mininet.topo import Topo
from mininet.util import irange

class CustomSFTopo( Topo ):
    def build(self):
        switches = [ self.addSwitch('s%s' % i ) for i in irange(1, 30)]
        # switches = [ self.addSwitch('s%s' % i ) for i in irange(1, 15)]
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30 = switches

        bw_low = 0.1
        bw_med = 1
        bw_high = 10

        delay_low = '1ms'
        delay_med = '50ms'
        delay_high = '100ms'
        delay_xhigh = '200ms'

        #scale free 20 non-duplicate links
        # self.addLink(s1, s2, bw=bw_high, delay=delay_high)
        # self.addLink(s3, s1, bw=bw_med, delay=delay_high)
        # self.addLink(s5, s1, bw=bw_low, delay=delay_low)
        # self.addLink(s7, s1, bw=bw_med, delay=delay_med)
        # self.addLink(s12, s1, bw=bw_high, delay=delay_med)
        # self.addLink(s15, s1, bw=bw_high, delay=delay_med)
        # self.addLink(s17, s1, bw=bw_low, delay=delay_med)
        # self.addLink(s20, s1, bw=bw_high, delay=delay_high)
        #
        # self.addLink(s2, s3, bw=bw_low, delay=delay_high)
        # self.addLink(s4, s2, bw=bw_med, delay=delay_high)
        # self.addLink(s9, s2, bw=bw_med, delay=delay_med)
        # self.addLink(s11, s2, bw=bw_high, delay=delay_med)
        # self.addLink(s16, s2, bw=bw_high, delay=delay_high)
        # self.addLink(s13, s2, bw=bw_med, delay=delay_high)
        # self.addLink(s19, s2, bw=bw_high, delay=delay_low)
        #
        # self.addLink(s3, s14, bw=bw_med, delay=delay_high)
        #
        # self.addLink(s8, s4, bw=bw_high, delay=delay_high)
        #
        # self.addLink(s5, s6, bw=bw_low, delay=delay_low)
        #
        # self.addLink(s10, s6, bw=bw_high, delay=delay_med)
        # self.addLink(s16, s6, bw=bw_high, delay=delay_high)
        #
        # self.addLink(s18, s8, bw=bw_low, delay=delay_low)

        # 30 nodes

        # self.addLink(s1, s2, bw=bw_high, delay=delay_high)
        # self.addLink(s1, s3, bw=bw_low, delay=delay_low)
        #
        #
        # self.addLink(s2, s3, bw=bw_high, delay=delay_low)
        # self.addLink(s4, s2, bw=bw_med, delay=delay_low)
        # self.addLink(s6, s2, bw=bw_high, delay=delay_med)
        # self.addLink(s10, s2, bw=bw_med, delay=delay_med)
        # self.addLink(s20, s2, bw=bw_low, delay=delay_med)
        # self.addLink(s24, s2, bw=bw_low, delay=delay_high)
        # self.addLink(s27, s2, bw=bw_high, delay=delay_high)
        # self.addLink(s29, s2, bw=bw_med, delay=delay_high)
        # self.addLink(s30, s2, bw=bw_med, delay=delay_med)
        #
        # self.addLink(s5, s3, bw=bw_high, delay=delay_high)
        # self.addLink(s6, s3, bw=bw_low, delay=delay_low)
        # self.addLink(s7, s3, bw=bw_low, delay=delay_high)
        # self.addLink(s8, s3, bw=bw_high, delay=delay_low)
        # self.addLink(s9, s3, bw=bw_low, delay=delay_low)
        # self.addLink(s10, s3, bw=bw_low, delay=delay_low)
        # self.addLink(s11, s3, bw=bw_high, delay=delay_med)
        # self.addLink(s13, s3, bw=bw_high, delay=delay_high)
        # self.addLink(s14, s3, bw=bw_low, delay=delay_low)
        # self.addLink(s15, s3, bw=bw_low, delay=delay_high)
        # self.addLink(s19, s3, bw=bw_med, delay=delay_low)
        # self.addLink(s21, s3, bw=bw_med, delay=delay_high)
        # self.addLink(s25, s3, bw=bw_med, delay=delay_low)
        #
        # self.addLink(s6, s18, bw=bw_high, delay=delay_low)
        # self.addLink(s6, s8, bw=bw_low, delay=delay_high)
        # self.addLink(s13, s6, bw=bw_high, delay=delay_high)
        # self.addLink(s14, s6, bw=bw_high, delay=delay_med)
        # self.addLink(s19, s6, bw=bw_high, delay=delay_low)
        # self.addLink(s23, s6, bw=bw_high, delay=delay_high)
        #
        # self.addLink(s10, s8, bw=bw_high, delay=delay_high)
        # self.addLink(s22, s8, bw=bw_med, delay=delay_high)
        #
        # self.addLink(s10, s12, bw=bw_med, delay=delay_low)
        # self.addLink(s28, s10, bw=bw_low, delay=delay_low)
        #
        # self.addLink(s19, s11, bw=bw_low, delay=delay_high)
        #
        # self.addLink(s26, s12, bw=bw_low, delay=delay_high)
        #
        # self.addLink(s14, s16, bw=bw_low, delay=delay_low)
        # self.addLink(s14, s18, bw=bw_low, delay=delay_high)
        #
        # self.addLink(s17, s16, bw=bw_low, delay=delay_med)
        # self.addLink(s27, s16, bw=bw_high, delay=delay_high)
        #
        # self.addLink(s19, s18, bw=bw_med, delay=delay_med)

        # 25 nodes

        self.addLink(s1, s2, bw=bw_med, delay=delay_low)
        self.addLink(s2, s3, bw=bw_high, delay=delay_xhigh)
        self.addLink(s2, s4, bw=bw_low, delay=delay_xhigh)
        self.addLink(s2, s20, bw=bw_high, delay=delay_xhigh)
        self.addLink(s3, s1, bw=bw_low, delay=delay_xhigh)
        self.addLink(s3, s4, bw=bw_low, delay=delay_xhigh)
        self.addLink(s5, s1, bw=bw_low, delay=delay_xhigh)
        self.addLink(s5, s6, bw=bw_low, delay=delay_xhigh)
        self.addLink(s5, s2, bw=bw_low, delay=delay_xhigh)
        self.addLink(s5, s16, bw=bw_low, delay=delay_xhigh)
        self.addLink(s5, s3, bw=bw_low, delay=delay_xhigh)
        self.addLink(s6, s4, bw=bw_low, delay=delay_xhigh)
        self.addLink(s6, s1, bw=bw_low, delay=delay_xhigh)
        self.addLink(s6, s12, bw=bw_low, delay=delay_xhigh)
        self.addLink(s6, s15, bw=bw_low, delay=delay_xhigh)
        self.addLink(s7, s1, bw=bw_low, delay=delay_xhigh)
        self.addLink(s7, s15, bw=bw_low, delay=delay_xhigh)
        self.addLink(s8, s4, bw=bw_low, delay=delay_xhigh)
        self.addLink(s8, s1, bw=bw_med, delay=delay_low)
        self.addLink(s8, s3, bw=bw_high, delay=delay_xhigh)
        self.addLink(s9, s6, bw=bw_low, delay=delay_xhigh)
        self.addLink(s10, s6, bw=bw_low, delay=delay_xhigh)
        self.addLink(s11, s3, bw=bw_low, delay=delay_xhigh)
        self.addLink(s13, s3, bw=bw_low, delay=delay_xhigh)
        self.addLink(s14, s3, bw=bw_low, delay=delay_xhigh)
        self.addLink(s14, s4, bw=bw_low, delay=delay_xhigh)
        self.addLink(s14, s1, bw=bw_low, delay=delay_xhigh)
        self.addLink(s14, s6, bw=bw_low, delay=delay_xhigh)
        self.addLink(s17, s1, bw=bw_low, delay=delay_xhigh)
        self.addLink(s17, s15, bw=bw_low, delay=delay_xhigh)
        self.addLink(s17, s25, bw=bw_low, delay=delay_xhigh)
        self.addLink(s18, s3, bw=bw_low, delay=delay_xhigh)
        self.addLink(s19, s2, bw=bw_low, delay=delay_xhigh)
        self.addLink(s19, s16, bw=bw_low, delay=delay_xhigh)
        self.addLink(s21, s2, bw=bw_low, delay=delay_xhigh)
        self.addLink(s22, s12, bw=bw_low, delay=delay_xhigh)
        self.addLink(s23, s3, bw=bw_low, delay=delay_xhigh)
        self.addLink(s24, s15, bw=bw_low, delay=delay_xhigh)



        # preferintial
        # self.addLink(s1, s3, bw=bw_low, delay=delay_med)

# self.addLink(s1, s4, bw=bw_med, delay=delay_low)
#
# self.addLink(s1, s5, bw=bw_low, delay=delay_med)
#
# self.addLink(s1, s6, bw=bw_low, delay=delay_high)
#
# self.addLink(s1, s7, bw=bw_high, delay=delay_med)
#
# self.addLink(s1, s8, bw=bw_high, delay=delay_med)
#
# self.addLink(s1, s9, bw=bw_med, delay=delay_med)
#
# self.addLink(s1, s10, bw=bw_low, delay=delay_high)
#
# self.addLink(s1, s15, bw=bw_med, delay=delay_med)
#
# self.addLink(s1, s22, bw=bw_high, delay=delay_low)
#
# self.addLink(s1, s23, bw=bw_low, delay=delay_low)
#
# self.addLink(s1, s25, bw=bw_high, delay=delay_high)
#
# self.addLink(s2, s3, bw=bw_high, delay=delay_med)
#
# self.addLink(s2, s4, bw=bw_med, delay=delay_high)
#
# self.addLink(s2, s6, bw=bw_low, delay=delay_med)
#
# self.addLink(s2, s7, bw=bw_low, delay=delay_low)
#
# self.addLink(s2, s16, bw=bw_med, delay=delay_med)
#
# self.addLink(s3, s5, bw=bw_low, delay=delay_med)
#
# self.addLink(s3, s8, bw=bw_high, delay=delay_low)
#
# self.addLink(s3, s10, bw=bw_med, delay=delay_high)
#
# self.addLink(s3, s11, bw=bw_low, delay=delay_high)
#
# self.addLink(s3, s13, bw=bw_med, delay=delay_low)
#
# self.addLink(s3, s18, bw=bw_high, delay=delay_med)
#
# self.addLink(s3, s19, bw=bw_high, delay=delay_high)
#
# self.addLink(s4, s15, bw=bw_low, delay=delay_low)
#
# self.addLink(s4, s23, bw=bw_high, delay=delay_low)
#
# self.addLink(s5, s25, bw=bw_low, delay=delay_high)
#
# self.addLink(s7, s9, bw=bw_low, delay=delay_low)
#
# self.addLink(s7, s12, bw=bw_low, delay=delay_low)
#
# self.addLink(s7, s13, bw=bw_high, delay=delay_high)
#
# self.addLink(s7, s16, bw=bw_low, delay=delay_high)
#
# self.addLink(s7, s17, bw=bw_high, delay=delay_low)
#
# self.addLink(s7, s19, bw=bw_high, delay=delay_low)
#
# self.addLink(s7, s20, bw=bw_med, delay=delay_med)
#
# self.addLink(s7, s21, bw=bw_med, delay=delay_high)
#
# self.addLink(s7, s22, bw=bw_high, delay=delay_med)
#
# self.addLink(s9, s14, bw=bw_low, delay=delay_med)
#
# self.addLink(s9, s24, bw=bw_low, delay=delay_low)
#
# self.addLink(s10, s11, bw=bw_high, delay=delay_low)
#
# self.addLink(s11, s12, bw=bw_med, delay=delay_high)
#
# self.addLink(s11, s14, bw=bw_high, delay=delay_low)
#
# self.addLink(s12, s17, bw=bw_med, delay=delay_low)
#
# self.addLink(s13, s18, bw=bw_med, delay=delay_low)
#
# self.addLink(s16, s21, bw=bw_high, delay=delay_low)
#
# self.addLink(s18, s20, bw=bw_high, delay=delay_med)
#
# self.addLink(s18, s24, bw=bw_high, delay=delay_high)




        self.addLink(h1, s20)
        self.addLink(h2, s8)

topos = { 'custom_scale_free_topo': CustomSFTopo }
