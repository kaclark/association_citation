import React from 'react';
import logo from './logo.svg';
import './App.css';
import token from "./token.json";
import { TodoistApi } from '@doist/todoist-api-typescript'

const api = new TodoistApi(token.token)
api.getTasks()
    .then((tasks) => console.log(tasks))
    .catch((error) => console.log(error))

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
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



