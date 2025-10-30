import re
text = "The agent's phone number is 408-555-1234. Call soon!"
match = re.search('phone', text)
print("Match found at:", match.span())
text2 = "My phone is a new phone"
matches = re.findall("phone", text2)
print("All matches:", matches)
for m in re.finditer("phone", text2):
    print("Match position:", m.span())
text3 = "My telephone number is 408-555-1234"
phone = re.search(r'\d{3}-\d{3}-\d{4}', text3)
print("Phone number:", phone.group())
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result = re.search(pattern, text3)
print("Area code:", result.group(1))
print("Prefix:", result.group(2))
print("Line number:", result.group(3))
print(re.search(r"man|woman", "This woman was here."))
print(re.findall(r'\S+at', "The cat sat on the mat"))
test = "This is a string! But it has punctuation."
clean = ' '.join(re.findall('[^!.? ]+', test))
print("Clean text:", clean)
text4 = "Find the long-ish words in this sentence."
print(re.findall(r'[\w]+-[\w]+', text4))
print(re.search(r'cat(fish|nap|claw)', "I saw a catfish."))

