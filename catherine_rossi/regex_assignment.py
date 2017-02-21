import re
def get_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape","bttu0bo"]
	matches = []
	for word in words:
 		if re.search(regex,word):
 			matches.append(word)
	return matches

#1 All words that contain a "v"
# print get_matching_words(r'v.')

#2 All words that contain a double-"s"
# print get_matching_words(r'ss+')

#3 All words that end with an "e"
#print get_matching_words(r'e$')

#4 All words that contain an "b", any character, then another "b"
#print get_matching_words(r'b.b')


#5 All words that contain a "b", at least one character, then another "b"
#print get_matching_words(r'b.+b')

#6 All words that contain an "b", any number of characters (including zero), then another "b"
#print get_matching_words(r'b\w+b')

#7 All words that include all five vowels in order
#print get_matching_words(r'a.*e.*i.*o.*u')

#8 All words that only use the letters in "regular expression" (each letter can appear any number of times)
#print get_matching_words(r'r+e+g+u+l+a+r+e+x+p+r+e+s+s+i+o+n')

#9 All words that contain a double letter
#print get_matching_words(r'.+')




