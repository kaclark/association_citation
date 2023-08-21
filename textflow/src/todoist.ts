import { TodoistApi } from '@doist/todoist-api-typescript'
import * as fs from 'fs';
const token = fs.readFileSync('/token.api', 'utf-8');

const api = new TodoistApi(token)

api.getTasks()
    .then((tasks) => console.log(tasks))
    .catch((error) => console.log(error))
