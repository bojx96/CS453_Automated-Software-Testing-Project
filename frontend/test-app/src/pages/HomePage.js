import "../App.css";
import cookieColour from "../img/cookieColour.png";
const HomePage = () => {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center", flexDirection: "column ", height: "100%" }}>
      <img id="cookielogo" src={cookieColour} alt="cookieColour" style={{ height: 448, width: 448 }} />
      <button id="eatcookie-button" class="Secondary-button">
        Eat Cookie
      </button>
    </div>
  );
};
export default HomePage;
