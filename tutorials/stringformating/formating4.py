#template string
from string import  Template
a1 = 'python'
n1 = 'cprogramin'
a2 = 'sinplilelalrn'
n = Template('Hello, welcome to $n1 programing')
print(n.substitute(n1 = a1))
