#!/bin/bash

python -m rich.markdown section1.md
printf "\n----------\nENTER for next section"
printf "\n----------\nRecord Note/Highlight\n#"
read lambda
if [ "$lambda" == "" ]; then
    echo ""
else
    timestamp=$(date +%T+%F)
    echo ${timestamp}: ${lambda} >> notes/section1.md
fi

python -m rich.markdown section2.md
printf "\n----------\nENTER for next section"
printf "\n----------\nRecord Note/Highlight\n#"
read lambda
if [ "$lambda" == "" ]; then
    echo ""
else
    timestamp=$(date +%T+%F)
    echo ${timestamp}: ${lambda} >> notes/section2.md
fi

python -m rich.markdown section3.md
printf "\n----------\nENTER for next section"
printf "\n----------\nRecord Note/Highlight\n#"
read lambda
if [ "$lambda" == "" ]; then
    echo ""
else
    timestamp=$(date +%T+%F)
    echo ${timestamp}: ${lambda} >> notes/section3.md
fi

python -m rich.markdown section4.md
printf "\n----------\nENTER for next section"
printf "\n----------\nRecord Note/Highlight\n#"
read lambda
if [ "$lambda" == "" ]; then
    echo ""
else
    timestamp=$(date +%T+%F)
    echo ${timestamp}: ${lambda} >> notes/section4.md
fi

python -m rich.markdown section5.md
printf "\n----------\nENTER for next section"
printf "\n----------\nRecord Note/Highlight\n#"
read lambda
if [ "$lambda" == "" ]; then
    echo ""
else
    timestamp=$(date +%T+%F)
    echo ${timestamp}: ${lambda} >> notes/section5.md
fi

python -m rich.markdown section6.md
printf "\n----------\nENTER for next section"
printf "\n----------\nRecord Note/Highlight\n#"
read lambda
if [ "$lambda" == "" ]; then
    echo ""
else
    timestamp=$(date +%T+%F)
    echo ${timestamp}: ${lambda} >> notes/section6.md
fi

python -m rich.markdown section7.md
printf "\n----------\nENTER for next section"
printf "\n----------\nRecord Note/Highlight\n#"
read lambda
if [ "$lambda" == "" ]; then
    echo ""
else
    timestamp=$(date +%T+%F)
    echo ${timestamp}: ${lambda} >> notes/section7.md
fi

python -m rich.markdown section8.md
printf "\n----------\nENTER for next section"
printf "\n----------\nRecord Note/Highlight\n#"
read lambda
if [ "$lambda" == "" ]; then
    echo ""
else
    timestamp=$(date +%T+%F)
    echo ${timestamp}: ${lambda} >> notes/section8.md
fi
