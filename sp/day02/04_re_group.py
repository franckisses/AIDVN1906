html = """
<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>
<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>
    <p class="content">
		Small white rabbit white and white
    </p>
</div>"""
import re
res = '<div class="animal">.*?title="(.*?)".*?"content">(.*?)</p>'
pattern = re.compile(res,re.S)
re_list = pattern.findall(html)
# print(re_list)
"""
[('Tiger', '\n\t\tTwo tigers two tigers run fast\n    '), 
 ('Rabbit', '\n\t\tSmall white rabbit white and white\n    ')]
"""
for i in re_list:
    print('animal',i[0].strip())
    print('statement',i[1].strip())
    print('*'*20)