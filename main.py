#--------------------------------------------
# NAME: SEUN OMOJO  LA
# STUDENT NUMBER: 7880480 
# COURSE: COMP 4820
#---------------------------------------------

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import time
import trie
import brute_force
import getopt, sys
# total arguments
n = len(sys.argv)

 # Options
options = "-b"
 
# Long options
long_options = "brute-force"

#copy the patterns to a new list. just because...
if sys.argv[n-1] == (options or long_options):
    patterns = sys.argv[2:n-1]
else:
    patterns = sys.argv[2:n]

fasta_records = list(SeqIO.parse(sys.argv[1], 'fasta'))
text = fasta_records[0].seq


#check to know if to use brute force approach
if (sys.argv[n-1] == (options or long_options)):
    print("Searching for patterns:",patterns,"in the sequence",sys.argv[1],"using the brute-force algorithm")
    start_time = time.time()
    result = brute_force.count_pattern_occurrences(text, patterns)
    end_time  = time.time()
    for string, count in result.items():
        print(f"Found pattern '{string}' {count} times")
    print( "Completed the search in",end_time - start_time, "seconds.")
    
else: #run aho corasick algorithm
    prefix_trie = trie.build_prefix_trie(patterns)
    trie.build_failure_links(prefix_trie)
    print("Searching for patterns:",patterns,"in the sequence",sys.argv[1],"using the aho-corasick algorithm")
    start_time = time.time()
    result = trie.search(text, patterns,prefix_trie)
    end_time  = time.time()
    for string, count in result.items():
        print(f"Found pattern '{string}' {count} times")
    print( "Completed the search in",end_time - start_time, "seconds.")