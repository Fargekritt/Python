text = "racecarabbaenterelephantmalayalam"
results = set()
text_length = len(text)
for idx, char in enumerate(text):

	# Check for longest odd palindrome(s)
	start, end = idx - 1, idx + 1
	while start >= 0 and end < text_length and text[start] == text[end]:
		results.add(text[start:end+1])	
		start -= 1
		end += 1

	start, end = idx, idx + 1
	while start >= 0 and end < text_length and text[start] == text[end]:
		results.add(text[start:end+1])	
		start -= 1
		end += 1
print(results)