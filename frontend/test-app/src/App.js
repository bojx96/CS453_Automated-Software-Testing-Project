import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <div>
        <input id="emailinput-textfield" type="text" placeholder="Email" />
      </div>
      <div>
        <input id="passwordinput-textfield" type="password" placeholder="Password" />
      </div>
      <div>
        <button id="loginbutton-button">Login Button</button>
      </div>
      <div>
        <button id="createaccount-button">Create Account</button>
      </div>
    </div>
  );
}

export default App;
