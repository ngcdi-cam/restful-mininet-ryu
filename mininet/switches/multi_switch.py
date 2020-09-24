
from mininet.log import error, warn, debug, info
from mininet.node import OVSSwitch

class MultiSwitch(OVSSwitch):
    "Custom Switch() subclass that connects to different controllers"
    def __init__(self, name, cmap, **kwargs):
        if type(cmap) is str:
            self.cmap = {}
            pairs = cmap.split('|')
            for pair in pairs:
                key, value = pair.split(":", 2)
                self.cmap[key] = value
        elif type(cmap) is dict:
            self.cmap = cmap
        else:
            raise Exception("Bad cmap type: %s" % type(cmap))
        super(MultiSwitch, self).__init__(name, **kwargs)

    def start(self, controllers):
        if self.cmap is None:
            return OVSSwitch.start(self, controllers)
        else:
            #info("Controllers %s\n" % controllers)
            controller_name = self.cmap.get(self.name)
            if controller_name is None:
                warn("No controller specified\n")
                return OVSSwitch.start(self, [])
            controllers_filtered = list(filter(lambda c: c.name == controller_name, controllers))
            if len(controllers_filtered) == 0:
               warn("Invalid controller %s specified\n" % controller_name)
            else:
               info("Connected to controller %s\n" % controllers_filtered[0])
            return OVSSwitch.start(self, controllers_filtered)

switches = { 'multi': MultiSwitch }
