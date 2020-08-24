from mininet.topo import Topo

class TestHopBwTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        bw_high = 100
        bw_low = 1

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(s1, s3, bw=bw_high)
        self.addLink(s3, s2, bw=bw_high)
        self.addLink(s1, s2, bw=bw_low)


topos = { 'test_hop_bw': TestHopBwTopo }
