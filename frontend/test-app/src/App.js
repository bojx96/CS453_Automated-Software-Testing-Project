import "./App.css";
import cookieLogo from "./img/cookieLogo.png";
import { Route, Routes, useLocation, useNavigate } from "react-router-dom";

import LandingPage from "./pages/LandingPage";
import CreatePage from "./pages/CreatePage";
import SettingsPage from "./pages/SettingsPage";
import HomePage from "./pages/HomePage";

function App() {
  const location = useLocation();
  let navigate = useNavigate();
  const routeChange = (buttonText) => {
    let path = buttonText;
    navigate(path);
  };
  return (
    <>
      {location.pathname != "/" && location.pathname != "/create" ? (
        <div>
          <div style={{ display: "flex", flexDirection: "row" }}>
            <div>
              <img id="cookielogo" src={cookieLogo} alt="cookieLogo" style={{ paddingLeft: 56, paddingTop: 17, paddingBottom: 17, height: 68, width: 68 }} />
            </div>
            <div style={{ display: "flex", flexDirection: "row", alignItems: "end" }}>
              <div style={{ paddingLeft: 88, paddingRight: 198 }}>
                <button id="home-button" class="bar-button" onClick={() => routeChange("/homepage")}>
                  Home
                </button>
              </div>
              <div style={{ paddingRight: 198 }}>
                <button id="mail-button" class="bar-button" onClick={() => routeChange("/mail")}>
                  Mail
                </button>
              </div>
              <div>
                <button id="settings-button" class="bar-button" style={{ paddingRight: 530 }} onClick={() => routeChange("/settings")}>
                  Settings
                </button>
              </div>
              <div>
                <button id="signout-button" class="bar-button" onClick={() => routeChange("/")}>
                  Signout
                </button>
              </div>
            </div>
          </div>
          <div class="line"></div>
        </div>
      ) : (
        <></>
      )}
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/create" element={<CreatePage />} />
        <Route path="/settings" element={<SettingsPage />} />
        <Route path="/homepage" element={<HomePage />} />
      </Routes>
    </>
  );
}

export default App;
