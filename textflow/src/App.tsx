import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import token from "./token.json";
import { TodoistApi } from '@doist/todoist-api-typescript'

var comm_arr:string[] = [];
//const [mcomm, setmcomm] = useState<Array<string>>([]);
const api = new TodoistApi(token.token)
api.getComments({ taskId: "7139027260"})
	.then((comments) => {
		//comments.forEach(x => { setmcomm(mcomm => [...mcomm, x.content]); });
		comments.forEach(x => { comm_arr.push(x.content);})
	})
	.catch((error) => console.log(error))
console.log(comm_arr)

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
	<ul>
          {comm_arr.map(item => <li key={item}>{item}</li>)}
        </ul>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;



