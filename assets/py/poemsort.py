#/usr/bin/env python
from collections import Counter


poem = '''Erected to the memory of Mrs Dermot O'Brien O commemorate me where there is water Canal water preferably so stilly Greeny at the heart of summer Brother Commemorate me thus beautifully Where by a lock niagarously roars The falls for those who sit in the tremendous silence Of mid-July No one will speak in prose Who finds his way to these Parnassian islands A swan goes by head low with many apologies Fantastic light looks through the eyes of bridges And look a barge comes bringing from Athy And other far-flung towns mythologies O commemorate me with no hero-courageous Tomb just a canal-bank seat for the passer-by'''

words = poem.split(' ')
words.sort()

# print words

wordcount = Counter([x.lower() for x in words])
print '<table>'
for word in wordcount:
	print '<tr><td>%s</td><td>%s</td></tr>' % (word, wordcount[word])

print '</table>'
