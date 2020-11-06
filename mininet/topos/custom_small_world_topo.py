from mininet.topo import Topo
from mininet.util import irange

class CustomSWTopo( Topo ):
    def build(self):
        switches = [ self.addSwitch('s%s' % i ) for i in irange(1, 25)]
        # switches = [ self.addSwitch('s%s' % i ) for i in irange(1, 15)]
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        # h3 = self.addHost('h3')
        # h4 = self.addHost('h4')
        # h5 = self.addHost('h5')

        #s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15 = switches
        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25 = switches
        #s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40 = switches

        bw_low = 0.1
        bw_med = 1
        bw_high = 10

        delay_low = '1ms'
        delay_med = '50ms'
        delay_high = '100ms'
        delay_xhigh = '200ms'

        # self.addLink(s1, s2, bw=bw_low, delay=delay_high)
        # self.addLink(s1, s3, bw=bw_high, delay=delay_med)
        # self.addLink(s1, s8, bw=bw_low, delay=delay_med)
        # self.addLink(s1, s14, bw=bw_low, delay=delay_med)
        # self.addLink(s1, s15, bw=bw_low, delay=delay_low)
        #
        # self.addLink(s2, s3, bw=bw_low, delay=delay_med)
        # self.addLink(s2, s11, bw=bw_low, delay=delay_med)
        # self.addLink(s2, s12, bw=bw_low, delay=delay_med)
        # self.addLink(s2, s15, bw=bw_low, delay=delay_high)
        #
        # self.addLink(s3, s4, bw=bw_low, delay=delay_low)
        # self.addLink(s3, s5, bw=bw_low, delay=delay_med)
        # self.addLink(s3, s9, bw=bw_high, delay=delay_med)
        #
        # self.addLink(s4, s5, bw=bw_low, delay=delay_high)
        # self.addLink(s4, s6, bw=bw_low, delay=delay_low)
        # self.addLink(s4, s11, bw=bw_low, delay=delay_low)
        #
        # self.addLink(s5, s7, bw=bw_low, delay=delay_med)
        # self.addLink(s5, s11, bw=bw_low, delay=delay_high)
        # self.addLink(s5, s14, bw=bw_low, delay=delay_low)
        #
        # self.addLink(s6, s7, bw=bw_low, delay=delay_high)
        # self.addLink(s6, s8, bw=bw_low, delay=delay_med)
        #
        # self.addLink(s7, s8, bw=bw_low, delay=delay_high)
        # self.addLink(s7, s9, bw=bw_low, delay=delay_med)
        #
        # self.addLink(s8, s9, bw=bw_low, delay=delay_high)
        #
        # self.addLink(s9, s10, bw=bw_low, delay=delay_high)
        # self.addLink(s9, s12, bw=bw_low, delay=delay_low)
        #
        # self.addLink(s10, s11, bw=bw_low, delay=delay_low)
        # self.addLink(s10, s14, bw=bw_low, delay=delay_low)
        #
        # self.addLink(s11, s13, bw=bw_low, delay=delay_low)
        #
        # self.addLink(s13, s14, bw=bw_low, delay=delay_high)
        # self.addLink(s13, s15, bw=bw_low, delay=delay_med)


        # self.addLink(s1, s2, bw=bw_med, delay=delay_med)
        # self.addLink(s1, s3, bw=bw_med, delay=delay_med)
        # self.addLink(s1, s24, bw=bw_high, delay=delay_med)
        # self.addLink(s2, s3, bw=bw_low, delay=delay_high)
        # self.addLink(s2, s27, bw=bw_med, delay=delay_high)
        # self.addLink(s2, s40, bw=bw_med, delay=delay_high)
        # self.addLink(s3, s4, bw=bw_high, delay=delay_low)
        # self.addLink(s3, s5, bw=bw_low, delay=delay_low)
        # self.addLink(s3, s9, bw=bw_low, delay=delay_low)
        # self.addLink(s4, s5, bw=bw_med, delay=delay_high)
        # self.addLink(s4, s6, bw=bw_high, delay=delay_low)
        # self.addLink(s5, s7, bw=bw_low, delay=delay_med)
        # self.addLink(s5, s10, bw=bw_high, delay=delay_med)
        # self.addLink(s6, s7, bw=bw_med, delay=delay_med)
        # self.addLink(s6, s8, bw=bw_high, delay=delay_high)
        # self.addLink(s6, s12, bw=bw_med, delay=delay_high)
        # self.addLink(s7, s8, bw=bw_high, delay=delay_high)
        # self.addLink(s7, s9, bw=bw_high, delay=delay_high)
        # self.addLink(s7, s10, bw=bw_low, delay=delay_med)
        # self.addLink(s8, s9, bw=bw_low, delay=delay_med)
        # self.addLink(s8, s20, bw=bw_low, delay=delay_med)
        # self.addLink(s8, s29, bw=bw_low, delay=delay_high)
        # self.addLink(s9, s10, bw=bw_high, delay=delay_med)
        # self.addLink(s9, s12, bw=bw_med, delay=delay_high)
        # self.addLink(s10, s11, bw=bw_high, delay=delay_low)
        # self.addLink(s10, s21, bw=bw_high, delay=delay_med)
        # self.addLink(s11, s13, bw=bw_low, delay=delay_high)
        # self.addLink(s11, s37, bw=bw_med, delay=delay_low)
        # self.addLink(s13, s14, bw=bw_high, delay=delay_low)
        # self.addLink(s13, s15, bw=bw_low, delay=delay_med)
        # self.addLink(s13, s17, bw=bw_high, delay=delay_high)
        # self.addLink(s14, s16, bw=bw_med, delay=delay_med)
        # self.addLink(s14, s26, bw=bw_low, delay=delay_med)
        # self.addLink(s15, s16, bw=bw_low, delay=delay_low)
        # self.addLink(s15, s17, bw=bw_high, delay=delay_high)
        # self.addLink(s15, s25, bw=bw_med, delay=delay_high)
        # self.addLink(s16, s17, bw=bw_low, delay=delay_med)
        # self.addLink(s16, s18, bw=bw_med, delay=delay_med)
        # self.addLink(s17, s18, bw=bw_med, delay=delay_med)
        # self.addLink(s17, s27, bw=bw_high, delay=delay_low)
        # self.addLink(s18, s19, bw=bw_med, delay=delay_low)
        # self.addLink(s18, s20, bw=bw_med, delay=delay_med)
        # self.addLink(s19, s20, bw=bw_med, delay=delay_high)
        # self.addLink(s19, s21, bw=bw_low, delay=delay_low)
        # self.addLink(s20, s21, bw=bw_high, delay=delay_low)
        # self.addLink(s20, s28, bw=bw_med, delay=delay_high)
        # self.addLink(s20, s31, bw=bw_med, delay=delay_high)
        # self.addLink(s21, s22, bw=bw_low, delay=delay_low)
        # self.addLink(s22, s23, bw=bw_low, delay=delay_med)
        # self.addLink(s22, s24, bw=bw_med, delay=delay_med)
        # self.addLink(s23, s24, bw=bw_med, delay=delay_med)
        # self.addLink(s23, s25, bw=bw_high, delay=delay_high)
        # self.addLink(s23, s39, bw=bw_low, delay=delay_high)
        # self.addLink(s24, s26, bw=bw_low, delay=delay_med)
        # self.addLink(s24, s40, bw=bw_low, delay=delay_med)
        # self.addLink(s25, s26, bw=bw_med, delay=delay_med)
        # self.addLink(s26, s28, bw=bw_med, delay=delay_med)
        # self.addLink(s26, s39, bw=bw_low, delay=delay_low)
        # self.addLink(s27, s29, bw=bw_med, delay=delay_high)
        # self.addLink(s28, s30, bw=bw_med, delay=delay_high)
        # self.addLink(s29, s30, bw=bw_med, delay=delay_high)
        # self.addLink(s29, s31, bw=bw_high, delay=delay_low)
        # self.addLink(s29, s37, bw=bw_low, delay=delay_low)
        # self.addLink(s30, s31, bw=bw_med, delay=delay_high)
        # self.addLink(s30, s32, bw=bw_high, delay=delay_med)
        # self.addLink(s31, s35, bw=bw_high, delay=delay_high)
        # self.addLink(s32, s33, bw=bw_med, delay=delay_med)
        # self.addLink(s32, s38, bw=bw_med, delay=delay_low)
        # self.addLink(s33, s34, bw=bw_low, delay=delay_med)
        # self.addLink(s33, s35, bw=bw_med, delay=delay_high)
        # self.addLink(s34, s35, bw=bw_low, delay=delay_low)
        # self.addLink(s34, s36, bw=bw_med, delay=delay_high)
        # self.addLink(s35, s36, bw=bw_low, delay=delay_low)
        # self.addLink(s35, s37, bw=bw_med, delay=delay_med)
        # self.addLink(s36, s37, bw=bw_med, delay=delay_med)
        # self.addLink(s36, s38, bw=bw_med, delay=delay_low)
        # self.addLink(s37, s38, bw=bw_low, delay=delay_low)
        # self.addLink(s38, s39, bw=bw_low, delay=delay_high)
        # self.addLink(s38, s40, bw=bw_med, delay=delay_high)
        # self.addLink(s39, s40, bw=bw_low, delay=delay_med)

        # 20 nodes

        # self.addLink(s1, s2, bw=bw_low, delay=delay_med)
        # self.addLink(s1, s3, bw=bw_med, delay=delay_med)
        # self.addLink(s1, s19, bw=bw_low, delay=delay_low)
        # self.addLink(s1, s20, bw=bw_low, delay=delay_med)
        # self.addLink(s2, s3, bw=bw_med, delay=delay_med)
        # self.addLink(s2, s8, bw=bw_med, delay=delay_med)
        # self.addLink(s2, s14, bw=bw_med, delay=delay_high)
        # self.addLink(s3, s4, bw=bw_med, delay=delay_low)
        # self.addLink(s3, s5, bw=bw_high, delay=delay_med)
        # self.addLink(s3, s12, bw=bw_high, delay=delay_med)
        # self.addLink(s4, s5, bw=bw_high, delay=delay_high)
        # self.addLink(s4, s6, bw=bw_low, delay=delay_low)
        # self.addLink(s4, s9, bw=bw_low, delay=delay_low)
        # self.addLink(s4, s14, bw=bw_low, delay=delay_med)
        # self.addLink(s5, s7, bw=bw_high, delay=delay_high)
        # self.addLink(s5, s11, bw=bw_low, delay=delay_low)
        # self.addLink(s5, s15, bw=bw_med, delay=delay_high)
        # self.addLink(s5, s17, bw=bw_med, delay=delay_med)
        # self.addLink(s6, s7, bw=bw_med, delay=delay_high)
        # self.addLink(s6, s8, bw=bw_high, delay=delay_med)
        # self.addLink(s7, s8, bw=bw_high, delay=delay_high)
        # self.addLink(s7, s9, bw=bw_high, delay=delay_high)
        # self.addLink(s7, s12, bw=bw_high, delay=delay_low)
        # self.addLink(s8, s9, bw=bw_med, delay=delay_low)
        # self.addLink(s8, s20, bw=bw_med, delay=delay_low)
        # self.addLink(s9, s10, bw=bw_med, delay=delay_low)
        # self.addLink(s10, s11, bw=bw_high, delay=delay_high)
        # self.addLink(s10, s19, bw=bw_med, delay=delay_med)
        # self.addLink(s11, s13, bw=bw_high, delay=delay_high)
        # self.addLink(s13, s14, bw=bw_low, delay=delay_high)
        # self.addLink(s13, s15, bw=bw_med, delay=delay_low)
        # self.addLink(s14, s16, bw=bw_high, delay=delay_med)
        # self.addLink(s15, s16, bw=bw_low, delay=delay_high)
        # self.addLink(s15, s17, bw=bw_low, delay=delay_low)
        # self.addLink(s16, s17, bw=bw_med, delay=delay_high)
        # self.addLink(s16, s18, bw=bw_high, delay=delay_med)
        # self.addLink(s17, s18, bw=bw_med, delay=delay_low)
        # self.addLink(s18, s19, bw=bw_med, delay=delay_low)
        # self.addLink(s18, s20, bw=bw_low, delay=delay_high)
        # self.addLink(s19, s20, bw=bw_high, delay=delay_med)

        #25 nodes

        self.addLink(s1, s2, bw=bw_low, delay=delay_high)
        self.addLink(s1, s25, bw=bw_low, delay=delay_high)
        self.addLink(s1, s3, bw=bw_low, delay=delay_high)
        self.addLink(s1, s7, bw=bw_low, delay=delay_high)
        self.addLink(s1, s18, bw=bw_low, delay=delay_high)
        self.addLink(s2, s3, bw=bw_low, delay=delay_high)
        self.addLink(s2, s7, bw=bw_low, delay=delay_high)
        self.addLink(s2, s4, bw=bw_low, delay=delay_high)
        self.addLink(s2, s19, bw=bw_low, delay=delay_high)
        self.addLink(s3, s4, bw=bw_low, delay=delay_high)
        self.addLink(s4, s5, bw=bw_high, delay=delay_high)
        self.addLink(s5, s6, bw=bw_high, delay=delay_high)
        self.addLink(s5, s21, bw=bw_high, delay=delay_high)
        self.addLink(s6, s7, bw=bw_high, delay=delay_high)
        self.addLink(s7, s8, bw=bw_high, delay=delay_high)
        self.addLink(s8, s9, bw=bw_med, delay=delay_low)
        self.addLink(s9, s10, bw=bw_med, delay=delay_low)
        self.addLink(s10, s11, bw=bw_low, delay=delay_high)
        self.addLink(s10, s16, bw=bw_med, delay=delay_low)
        self.addLink(s11, s12, bw=bw_low, delay=delay_high)
        self.addLink(s12, s13, bw=bw_low, delay=delay_high)
        self.addLink(s12, s22, bw=bw_low, delay=delay_high)
        self.addLink(s13, s14, bw=bw_low, delay=delay_high)
        self.addLink(s13, s24, bw=bw_low, delay=delay_high)
        self.addLink(s14, s15, bw=bw_low, delay=delay_high)
        self.addLink(s15, s16, bw=bw_low, delay=delay_high)
        self.addLink(s16, s17, bw=bw_med, delay=delay_low)
        self.addLink(s17, s18, bw=bw_med, delay=delay_low)
        self.addLink(s17, s23, bw=bw_low, delay=delay_high)
        self.addLink(s18, s19, bw=bw_low, delay=delay_high)
        self.addLink(s19, s20, bw=bw_med, delay=delay_low)
        self.addLink(s20, s21, bw=bw_high, delay=delay_high)
        self.addLink(s21, s22, bw=bw_low, delay=delay_high)
        self.addLink(s22, s23, bw=bw_low, delay=delay_high)
        self.addLink(s23, s24, bw=bw_low, delay=delay_high)
        self.addLink(s24, s25, bw=bw_low, delay=delay_high)





        self.addLink(h1, s8)
        self.addLink(h2, s20)

        # self.addLink(h3, s3)
        # self.addLink(h4, s7)
        #
        # self.addLink(h5, s9)



topos = { 'custom_small_world_topo': CustomSWTopo }
