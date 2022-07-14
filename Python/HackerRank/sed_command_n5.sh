#https://www.hackerrank.com/challenges/sed-command-5/problem?h_r=profile
sed -E 's/([[:digit:]]{4}) ([[:digit:]]{4}) ([[:digit:]]{4}) ([[:digit:]]{4})/\4 \3 \2 \1/'