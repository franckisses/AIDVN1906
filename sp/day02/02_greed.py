# fake_useragent
import re
html = """
<h1><p>床前明月光</p></h1>
<h1><p>疑是地上霜</p></h1>
"""

pattern = re.compile('<h1><p>.*</p></h1>',re.S)
r_list = pattern.findall(html)
print(r_list)

pattern = re.compile('<h1><p>.*?</p></h1>',re.S)
r_list = pattern.findall(html)
print(r_list)