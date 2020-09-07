from mininet.topo import Topo

class CustomTopo( Topo ):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        # h3 = self.addHost('h3')
        # h4 = self.addHost('h4')
        # h5 = self.addHost('h5')
        # h6 = self.addHost('h6')
        # h7 = self.addHost('h7')
        # h8 = self.addHost('h8')
        # h9 = self.addHost('h9')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')
        s13 = self.addSwitch('s13')
        s14 = self.addSwitch('s14')

        bw_low = 0.1
        bw_med = 1
        bw_high = 10

        delay_low = '0ms'
        delay_med = '20ms'
        delay_high = '40ms'

        self.addLink(h1, s1)
        self.addLink(h2, s14)

        # Access Nodes
        self.addLink(s1, s7, bw=bw_high, delay=delay_low)
        self.addLink(s1, s8, bw=bw_high, delay=delay_low)
        self.addLink(s2, s7, bw=bw_low, delay=delay_high)
        self.addLink(s2, s8, bw=bw_low, delay=delay_high)
        self.addLink(s2, s9, bw=bw_low, delay=delay_high)
        self.addLink(s3, s9, bw=bw_low, delay=delay_high)
        self.addLink(s3, s10, bw=bw_low, delay=delay_high)
        self.addLink(s4, s9, bw=bw_low, delay=delay_high)
        self.addLink(s4, s10, bw=bw_low, delay=delay_high)
        self.addLink(s5, s11, bw=bw_low, delay=delay_high)
        self.addLink(s6, s11, bw=bw_low, delay=delay_high)
        self.addLink(s5, s10, bw=bw_low, delay=delay_high)
        self.addLink(s6, s10, bw=bw_low, delay=delay_high)

        # Met
        self.addLink(s7, s12, bw=bw_high, delay=delay_low)
        self.addLink(s8, s12, bw=bw_high, delay=delay_med)
        self.addLink(s9, s12, bw=bw_low, delay=delay_high)
        self.addLink(s10, s12, bw=bw_low, delay=delay_high)
        self.addLink(s11, s12, bw=bw_low, delay=delay_high)

        self.addLink(s9, s13, bw=bw_low, delay=delay_high)
        self.addLink(s10, s13, bw=bw_low, delay=delay_high)
        self.addLink(s11, s13, bw=bw_low, delay=delay_high)
        self.addLink(s11, s14, bw=bw_low, delay=delay_high)

        # Core
        self.addLink(s12, s13, bw=bw_low, delay=delay_low)
        self.addLink(s12, s14, bw=bw_high, delay=delay_high)
        self.addLink(s13, s14, bw=bw_low, delay=delay_low)

topos = { 'custom': CustomTopo }
