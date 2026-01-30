import re

# text = "python is a programming language."
# res = re.search("python", text)

# if res:
#     print("Match found:", res.group())

text="my number is 1234567890 and 9872654210."
# num=re.findall("\d{10}",text)
# print("Phone numbers found:", num)

# for match in re.finditer("\d{10}", text):
#     print("Phone number found:", match.start(),"to", match.end())


text="my number is 1234567890"
masked=re.sub("\d{6}", "XXXXXX", text)
print("Masked text:", masked)


