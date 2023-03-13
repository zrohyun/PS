#https://leetcode.com/problems/word-frequency/
#https://stackoverflow.com/questions/10552803/how-to-create-a-frequency-list-of-every-word-in-a-file

# Read from the file words.txt and output the word frequency list to stdout.

# 177ms runtime
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r |awk '{print $2,$1}'

# 0ms runtime
#cat words.txt | tr -s [:blank:] '\n' | sort | uniq -c | sort -nr -k 1 | awk '{print $2, $1}'

# cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1 }'
# tr -s: truncate the string with target string, but only remaining one instance (e.g. multiple whitespaces)

# sort: To make the same string successive so that uniq could count the same string fully and correctly.

# uniq -c: uniq is used to filter out the repeated lines which are successive, -c means counting

# sort -r: -r means sorting in descending order

# awk '{ print $2, $1 }': To format the output, see here.