from mininet.topo import Topo

class LinearLimitedBwTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        bw_high = 2
        bw_low = 1

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(s1, s3, bw=1.5, delay='50ms')
        self.addLink(s3, s2, bw=1.5, delay='50ms')

        self.addLink(s1, s4, bw=1, delay='20ms')
        self.addLink(s4, s2, bw=1, delay='20ms')

topos = { 'linear_limited_bw': LinearLimitedBwTopo }
