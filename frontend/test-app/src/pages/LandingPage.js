const LandingPage = () => {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center", flexDirection: "column ", height: "100vh" }}>
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
};

export default LandingPage;
