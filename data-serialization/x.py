import xml.etree.ElementTree as ET
root = ET.fromstring('<?xml version="1.0" encoding="UTF-8"?><book><isbn>978026251875</isbn><title>Structure and Interpretation of Computer Programs - 2nd edition</title></book>');
book = {child.tag: child.text for child in root}
print(book)


root1 = ET.Element('book')
isbn = ET.SubElement(root1,'isbn')
isbn.text = '9780262510875'
title = ET.SubElement(root1,'title')
title.text = 'Structure and Interpretation of Computer Programs - 2nd edition'
ET.dump(root1)


