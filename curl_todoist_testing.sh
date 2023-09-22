#!/bin/bash

#initialize 
#input Bearer token from json(protected with .gitignore)
TOKEN=$(jq -r .token token.json)

#jq -r '.[] | "\(.content)"'
pull_reading_journal () {
    COMMENTS=$(curl "https://api.todoist.com/rest/v2/comments?task_id=7250931521" -H "Authorization: Bearer $TOKEN" | jq -r '.[] | "\(.content)@@@"')
    #for some reason the @@@ gets replaced but the newline character does not seem to register
    echo -e $(echo -e $COMMENTS | tr "@@@" "\n")

}

pull_reading_journal
