import "./App.css";
import { GoogleOAuthProvider } from "@react-oauth/google";
import Login from "./login";

function App() {
  console.log(process.env.REACT_APP_GOOGLE_KEY);
  return (
    <GoogleOAuthProvider clientId={process.env.REACT_APP_GOOGLE_KEY}>
      <div className="App"></div>
      <Login />
    </GoogleOAuthProvider>
  );
}

export default App;
