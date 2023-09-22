#!/bin/bash

#initialize 
#input Bearer token from json(protected with .gitignore)
TOKEN=$(jq -r .token token.json)

pull_reading_journal () {
#issue: newline not rendering!!
    echo -e $(curl "https://api.todoist.com/rest/v2/comments?task_id=7250931521" -H "Authorization: Bearer $TOKEN" | jq -r '.[] | "\(.content)\n"')

}

pull_reading_journal
