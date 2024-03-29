import { useNavigate } from "react-router-dom";

const CreatePage = () => {
  let navigate = useNavigate();
  const routeChange = (buttonText) => {
    let path = buttonText;
    navigate(path);
  };
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center", flexDirection: "column ", height: "100vh" }}>
      <div>
        <input id="registeremail-textfield" type="email" placeholder="Input Email *" />
      </div>
      <div>
        <input id="registerpassword-textfield" type="password" placeholder="Input Password *" required />
      </div>
      <div>
        <input id="confirmpassword-textfield" type="password" placeholder="Confirm Password *" required />
      </div>
      <div>
        <button id="registeraccount-button" onClick={() => routeChange("/")}>
          {" "}
          Register Account
        </button>
      </div>
      <div>
        <button id="registercancel-button" onClick={() => routeChange("/")}>
          Cancel
        </button>
      </div>
    </div>
  );
};

export default CreatePage;
