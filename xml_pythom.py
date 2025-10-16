import xml.etree.ElementTree as ET

xml_data = """
<user>
    <id>1</id>
    <name>John</name>
    <last_name>Doe</last_name>
</user>
"""

root = ET.fromstring(xml_data)

print(f"USER_ID: {root.find("id").text}")