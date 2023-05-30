import "../App.css";
const SettingsPage = () => {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center", flexDirection: "column ", height: "100%" }}>
      <div style={{ padding: 32, paddingTop: 150, display: "flex", flexDirection: "column" }}>
        <text class="Text-box-char">Change Password</text>
        <input id="changepassword-textfield" class="Text-box" required />
      </div>
      <div style={{ display: "flex", flexDirection: "column" }}>
        <text class="Text-box-char">Confirm Password</text>
        <input id="confirmchange-textfield" class="Text-box" type="text" required />
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
