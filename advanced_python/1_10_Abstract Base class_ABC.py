# Abstraction of a real entity
# Abstract Base Class (ABC) is a Python module that provides the infrastructure for defining custom abstract base classes.
# An abstract base class is a class that cannot be instantiated.
# An abstract base class is a class that defines abstract methods.
# An abstract method is a method that is declared in the abstract base class but does not have an implementation.

#  Useful for creating plugins - Example : Plugin System - CSv plugin, JSON plugin, XML plugin
#  Useful for creating a framework - Example : Django framework


from abc import ABC, abstractmethod
class Plugin(ABC):
    @abstractmethod
    def process(self, data):
        pass


class JSONPlugin(Plugin):
    def process(self, data):
        import json
        return json.loads(data)
Plugin.register(JSONPlugin)

class XMLPlugin(Plugin):
    def process(self, data):
        import xml.etree.ElementTree as ET
        return ET.fromstring(data)
        root = tree.getroot()
        for tag in tree.findall('key'):
            print(tag.tag, tag.attrib)

Plugin.register(XMLPlugin)
def run_plugin(plugin, data):
    return plugin.process(data)


# Usage
json_plugin = JSONPlugin()
xml_plugin = XMLPlugin()

data = '{"key": "value"}'
print(run_plugin(json_plugin, data))  # Output: {'key': 'value'}

data = '<root><key>value</key></root>'
print(run_plugin(xml_plugin, data))  # Output: <Element 'root' at 0x...>

data = '<root><name>nishanth</key></root>'
print(run_plugin(xml_plugin, data))