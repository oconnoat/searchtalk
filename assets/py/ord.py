
string = u'CENDARI IS A RESEARCH INFRASTRUCTURE PROJECT AIMED AT INTEGRATING DIGITAL ARCHIVES FOR MEDIEVAL AND MODERN EUROPEAN HISTORY'

chars = ''

for character in string:
    chars += str(ord(character))+', '

print string
print chars
