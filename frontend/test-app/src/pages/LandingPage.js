import "../App.css";
import { useNavigate } from "react-router-dom";

const LandingPage = () => {
  let navigate = useNavigate();
  const routeChange = (buttonText) => {
    let path = buttonText;
    navigate(path);
  };
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center", flexDirection: "column ", height: "100vh" }}>
      <div style={{ display: "flex", padding: 32, flexDirection: "column" }}>
        <text class="Text-box-char">Email</text>
        <input id="emailinput-textfield" type="text" class="Text-box" />
      </div>
      <div style={{ display: "flex", flexDirection: "column" }}>
        <text class="Text-box-char">Password</text>
        <input id="passwordinput-textfield" type="password" class="Text-box" />
      </div>
      <div style={{ padding: 32 }}>
        <button id="loginbutton-button" class="Primary-button" onClick={() => routeChange("/homepage")}>
          Login Button
        </button>
      </div>
      <div>
        <button id="createaccount-button" class="Secondary-button" onClick={() => routeChange("/create")}>
          Create Account
        </button>
      </div>
    </div>
  );
};

export default LandingPage;
