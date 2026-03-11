import { useState } from "react";
import { GoogleLogin } from "@react-oauth/google";
import { jwtDecode } from "jwt-decode";
import axios from "axios";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const sendToken = async (token) => {
    console.log(token);
    try {
      const res = await axios.post("http://localhost:5000/login", {
        token: token,
      });
      console.log(res);
    } catch (err) {
      alert("로그인 실패");
      console.log(err);
    }
  };

  const handleSuccess = async (res) => {
    // google 에서 발급받은 jwt token
    const google_token = res.credential;
    sendToken(google_token);
    //console.log(decoded);

    // 토큰 확인용
    const decoded = jwtDecode(google_token);
    console.log(decoded);
    // google 에서 토큰 받았을 때에도 google이 토큰 관련 키가 해킹 될 수 있으므로
    // 반드시 토큰을 한번 더 암호화 해주는 것이 안전함
  };
  const handleError = () => {
    alert("로그인에 실패 하셨습니다.");
  };

  return (
    <>
      <GoogleLogin onSuccess={handleSuccess} onError={handleError} />
    </>
  );
}

export default Login;
