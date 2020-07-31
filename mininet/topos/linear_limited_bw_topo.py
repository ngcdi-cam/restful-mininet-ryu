from mininet.topo import Topo

class LinearLimitedBwTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        bw = 1

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(s1, s2, bw=bw)
        self.addLink(h3, s1)

topos = { 'linear_limited_bw': LinearLimitedBwTopo }
