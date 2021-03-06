#Import library essentials
from sumy.parsers.plaintext import PlaintextParser 
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer 
import time
import os
import subprocess

def main():
	for i in range (1,11):

		start_time = time.time()

		filename = "input/"+str(i)+".txt"
		#filename = "plain_text.txt" #name of the plain-text file
		cmd = "wc -m "+filename
		wc = subprocess.check_output(cmd, shell=True)
		data = open("lexrank.csv", "a")
		op = open("output_lexrank.txt", "a")

		parser = PlaintextParser.from_file(filename, Tokenizer("english"))
		summarizer = LexRankSummarizer()

		summary = summarizer(parser.document, 5) #Summarize the document in 5 sentences

		op.write(filename+"\n")
		for sentence in summary:
			op.write(str(sentence))
			print sentence

		new_time = time.time() - start_time
		print "Time: ", new_time
		print wc
		l = wc.split()
		#print l[0]
		string = l[0]+" , "+str(new_time)+"\n"
		print string
		op.write("\n"+string+"\n")
		data.write(string)

	data.close()
	op.close()

if __name__ == "__main__":
	main()
