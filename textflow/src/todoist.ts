import { TodoistApi } from '@doist/todoist-api-typescript'
import * as fs from 'fs';
const rawToken = fs.readFileSync('token.api', 'utf-8');
const token = rawToken.trim()
const api = new TodoistApi(token)

api.getTasks()
    .then((tasks) => console.log(tasks))
    .catch((error) => console.log(error))
