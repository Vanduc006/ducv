import re
import os
txt = open('bai1_text.txt', 'r')
regex1 = re.compile(r'ha')
kq = regex1.search(txt.read())
print(kq)
# bài này học về regex nhg chưa hiểu =(