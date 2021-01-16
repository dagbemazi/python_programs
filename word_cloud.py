from wordcloud import WordCloud


def word_cloud(file_name, uninteresting_words):
	"""
	A word cloud generator
	"""
	# Initialize the dict to store word and count
	frequency = {}

	# Read the lines of the file
	with open(file_name, encoding="utf8") as file:
		lines = file.read()

	# Split the words into a list
	new_word = lines.lower().split()
	for word in new_word: # Iterate through the list
		# Word must be alphabetic and must
		# not be an uninteresting word e.g "and"
		if word.isalpha() and word not in uninteresting_words:
			# Search for word in dictionary
			# if not found, the dict is updated with the word
			# else the count for the word is incremented 
			if word not in frequency:
				frequency[word] = 0
			frequency[word] += 1
	return frequency

# List of words that must be excluded in word cloud
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

frequencies = word_cloud("your_textfile.txt", uninteresting_words)

# Create instance of class
cloud = WordCloud()
# Pass the frequency into the frequency counter
cloud.generate_from_frequencies(frequencies)
# Create the image file
cloud.to_file("sample.jpg")