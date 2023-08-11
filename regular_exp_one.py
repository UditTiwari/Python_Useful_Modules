#Regular Expressions allow us to serach fo =r genreral patters in text data!
#EXAMOL E-  a simple Email format  user@email.com
# We know in this case we re looking for a pettern 
#"text" + "@" + "text"  + ".com" 
import re

text = "The agent's phone number is 408-555-1234.Call soon!"


print("phone"  in text)

pattern = 'phone'
#serach() -return back first match object
match = re.search(pattern,text)
print(match.span())
print(match.start())
print(match.end())

text2 = "my phone once , my phone twice"

#findall() return thr list of all the matches
matches = re.findall('phone',text2)
# print(matches)

#matchiter - its combination of serach() and findall() 
for matchh in re.finditer('phone',text2):
    # print(matchh)
    print(match.span())
    print(matchh.group())