import "../App.css";
const SettingsPage = () => {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center", flexDirection: "column ", height: "100%" }}>
      <div style={{ padding: 32, paddingTop: 150 }}>
        <input id="changepassword-textfield" class="Text-box" placeholder="Change Password *" />
      </div>
      <div>
        <input id="confirmchange-textfield" class="Text-box" type="text" placeholder="Confirm Password *" />
      </div>
      <div style={{ padding: 32 }}>
        <button id="changesubmit-button" class="Primary-button">
          Change Password
        </button>
      </div>
    </div>
  );
};

export default SettingsPage;
