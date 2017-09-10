from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import time
import os
import subprocess

#import urllib3
#urllib3.disable_warnings()
#logging.captureWarnings(True)

def main():
	for i in range (1,11):

		start_time = time.time()

		filename = "input/"+str(i)+".txt" #name of the plain-text file
		cmd = "wc -m "+filename
		wc = subprocess.check_output(cmd, shell=True)
		data = open("lsa.csv", "a")
		op = open("output_lsa.txt", "a")

		LANGUAGE = "english"
		SENTENCES_COUNT = 5		#Summarize the document in 5 sentences

		op.write(filename+"\n")
	
		# url = "http://nlp.stanford.edu/IR-book/html/htmledition/contents-1.html"
		# url = "http://research.microsoft.com/pubs/77563/emnlp_svore07.pdf"
		# url = "https://www.quora.com/topic/Document-Summarization?share=1"
		# url = "http://askubuntu.com/questions/73160/how-do-i-find-the-amount-of-free-space-on-my-hard-drive"
		# url = "https://en.wikipedia.org/wiki/Automatic_summarization#Unsupervised_approaches:_TextRank_and_LexRank"
		# parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
		# or for plain text files
		parser = PlaintextParser.from_file(filename, Tokenizer(LANGUAGE))
		stemmer = Stemmer(LANGUAGE)

		summarizer = Summarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)

		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			op.write(str(sentence))
			print(sentence)

		time_now = time.time() - start_time
		print("Time: ", time_now)
		print(wc)
		l = wc.split()
		string = l[0]+" ,"+str(time_now)+"\n"
		op.write("\n"+string+"\n")
		data.write(string)

	data.close()
	op.close()
	
if __name__ == "__main__":
	main()
