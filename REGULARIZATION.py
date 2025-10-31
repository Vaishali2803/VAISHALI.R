import re
txt='the agent phone-number is 4085551234. Calling  the agent Soon!'
t='408-555-1234'
match=re.search('phone',txt)
print(match.start()) 
print(match.end())
print(match.span())
print(re.findall("agent",txt)) 
print(re.search(r'\d+',txt).group())  
print("Area code:", re.search(r'\d+',t).group()) 
print("Line number:",re.search(r'\d{4}+',t).group()) 
print(re.search(r"phone|email",txt))
print(re.findall(r'\S+er',txt)) 
print(' '.join(re.findall('[^!.]+',txt)))
print(re.findall(r'[\w]+-[\w]+',txt)) 
print(re.search(r'Call(ing|ed|er)',txt))
