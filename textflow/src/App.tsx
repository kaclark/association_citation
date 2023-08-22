import React from 'react';
import logo from './logo.svg';
import './App.css';
import token from "./token.json";
import { TodoistApi } from '@doist/todoist-api-typescript'

function parse_todo(comments) {
	let comm_arr:string[] = new Array(comments.length);
	comments.forEach(x => { comm_arr.push(x.content); });
	return comm_arr;
}

function get_comments(){
    const api = new TodoistApi(token.token)
    let comment_set = api.getComments({ taskId: "7139027260"})
	    .then((comments) => parse_todo(comments))
	    .catch((error) => console.log(error))
    console.log(comment_set)
}

get_comments()

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
	Coming Soon!
        </p>
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



