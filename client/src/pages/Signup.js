import { useState, useContext } from "react";
import { Link } from "react-router-dom";
import { AuthContext } from "../components/AuthContext";

function Signup() {
  const { setUser } = useContext(AuthContext)
  const [loginInfo, setLoginInfo] = useState({
    first_name: "",
    username: "",
    password: "",
    email: "",
  });
  const handleLoginChange = (e) => {
    setLoginInfo({ ...loginInfo, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("/api/sign_up", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(loginInfo),
    })
    .then((r) => r.json())
    .then((data) => {
      setUser(data);
    });
  };

  return (
    <main>
      <div className="signupMain">
        <div className="logoContainer"></div>
        <div className="titleContainer">
          <h1 className="loginTitle">Time Capsule Signup</h1>
        </div>
        <form className="loginForm" onSubmit={handleSubmit}>
        <div className="input-container">
            <label htmlFor="first_name">First Name: </label>
            <input
              value={loginInfo.first_name}
              id="first_name"
              name="first_name"
              onChange={handleLoginChange}
            />
          </div>
          <div className="input-container">
            <label htmlFor="username">Username: </label>
            <input
              value={loginInfo.username}
              id="username"
              name="username"
              onChange={handleLoginChange}
            />
          </div>
          <div className="input-container">
            <label htmlFor="email"> Email: </label>
            <input
              value={loginInfo.email}
              id="email"
              name="email"
              onChange={handleLoginChange}
            />
          </div>
          <div className="input-container">
            <label htmlFor="password">Password: </label>
            <input
              onChange={handleLoginChange}
              value={loginInfo.password}
              type="password"
              id="password"
              name="password"
            />
            <div>
              <input className="button" type="submit" value="Signup" />
            </div>
          </div>
        </form>
        <p className="font">
          Already have an account? <Link to="/login" className="links">Login</Link>
        </p>
      </div>
    </main>
  );
}

export default Signup;