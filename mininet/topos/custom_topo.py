from mininet.topo import Topo

class CustomTopo( Topo ):
    def build(self):
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )
        h9 = self.addHost( 'h9' )

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

        bandwidth = 100
        core_bw = 1000

        self.addLink(h1, s1, bw=bandwidth)
        self.addLink(h2, s2, bw=bandwidth)
        self.addLink(h3, s3, bw=bandwidth)
        self.addLink(h4, s4, bw=bandwidth)
        self.addLink(h5, s5, bw=bandwidth)
        self.addLink(h6, s6, bw=bandwidth)
        self.addLink(h7, s12, bw=core_bw)
        self.addLink(h8, s13, bw=core_bw)
        self.addLink(h9, s14, bw=core_bw)

        # Access Nodes
        self.addLink(s1, s7, bw=bandwidth)
        self.addLink(s1, s8, bw=bandwidth)
        self.addLink(s2, s7, bw=bandwidth)
        self.addLink(s2, s8, bw=bandwidth)
        self.addLink(s2, s9, bw=bandwidth)
        self.addLink(s3, s9, bw=bandwidth)
        self.addLink(s3, s10, bw=bandwidth)
        self.addLink(s4, s9, bw=bandwidth)
        self.addLink(s4, s10, bw=bandwidth)
        self.addLink(s5, s11, bw=bandwidth)
        self.addLink(s6, s11, bw=bandwidth)
        self.addLink(s5, s10, bw=bandwidth)
        self.addLink(s6, s10, bw=bandwidth)

        # Met
        self.addLink(s7, s12, bw=bandwidth)
        self.addLink(s8, s12, bw=bandwidth)
        self.addLink(s9, s12, bw=bandwidth)
        self.addLink(s10, s12, bw=bandwidth)
        self.addLink(s11, s12, bw=bandwidth)

        self.addLink(s9, s13, bw=bandwidth)
        self.addLink(s10, s13, bw=bandwidth)
        self.addLink(s11, s13, bw=bandwidth)
        self.addLink(s11, s14, bw=bandwidth)

        # Core
        self.addLink(s12, s13, bw=core_bw)
        self.addLink(s12, s14, bw=core_bw)
        self.addLink(s13, s14, bw=core_bw)

topos = { 'custom': CustomTopo }
