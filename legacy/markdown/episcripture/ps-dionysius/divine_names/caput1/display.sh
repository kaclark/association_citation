#!/bin/bash
#usage ./display.sh Markdown NoteFile

PURPLE='\033[0;35m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' 

python -m rich.markdown $1
printf "\n\n\n${PURPLE}ENTER for next section,${NC} or\n"
printf "${BLUE}Record Note/Highlight\n#${NC}"
read lambda
if [ "$lambda" == "" ]; then
    echo ""
else
    printf "\nConfirm Save? (Y/N): "
    read res
    if [ "$res" == "Y" ]; then
    	timestamp=$(date +%T+%F)
    	echo ${timestamp}: ${lambda} >> $2
	printf "${GREEN}Note Recorded${NC}\n"
    else
	printf "${PURPLE}Note Discarded${NC}\n"
    fi
fi
