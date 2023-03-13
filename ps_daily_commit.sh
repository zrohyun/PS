#! /bin/bash

#echo $SHELL

cd /Users/0hyun/Desktop/PS

IFS=$'\n'
gitstatus=( $(git status -su) )


function commit(){
for i in ${gitstatus[@]}
do
  IFS=' ';
  arr=( $i )

  t=${arr[0]}
  fname=${arr[1]} 

  if [[ $t == 'M' ]]; then 
    git add $fname
    break
  elif [[ $t == 'A' ]]; then echo 'add' $fname
  else echo ${arr[@]};

  fi
  
done
}  

function commit_one_by_one(){
IFS=' ';
arr=( ${gitstatus[0]} )
type=${arr[0]}

# fpath and file name separate
fpath=${arr[1]}
fname=( $(echo $fpath | tr '/' ' ') )
fname=${fname[${#fname[@]}-1]} # file_name = last index

time=$(LANG=en_us_88591;date '+%Y-%m-%d %a')
echo -e $"\n\n$time\n-----------------------------------------------------" >> /Users/0hyun/Desktop/PS/log.log

git add $fpath
if [[ $type == 'M' ]]; then
  git commit -m "M $fname"
  #elif [[ $type == 'A' ]]; then echo 'add' $fname
else
  git commit -m "A $fname" 
fi
}
#commit

commit_one_by_one
echo -e $"\nFINISH\n"
cd ~

#crontab -e
#10 00 * * * /bin/bash ~/Desktop/PS/ps_daily_commit.sh >> ~/Desktop/PS/log.log 2>&1

