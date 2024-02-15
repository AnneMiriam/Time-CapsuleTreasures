import { useState, useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { AuthContext } from "../components/AuthContext";

function Login() {
  const { setUser } = useContext(AuthContext); // Access setUser from AuthContext
  const navigate = useNavigate()
  const [loginInfo, setLoginInfo] = useState({ username: "", password: "" });
  
  
  const handleLoginChange = (e) => {
    setLoginInfo({ ...loginInfo, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(loginInfo),
    })
      .then((r) => {
        if (!r.ok) {
          throw new Error("Login failed");
        }
        return r.json();
      })
      .then((data) => {
        localStorage.setItem("user", JSON.stringify(data)); 
        setUser(data);
        navigate('/user_home');
      })
      .catch((e) => {
        console.error(e);
      });
  };

  return (
    <main>
      <div></div>
      <div className="loginMain">
        <div className="titleContainer">
          <h1 className="loginTitle">Time Capsule Login</h1>
        </div>
        <form className="loginForm" onSubmit={handleSubmit}>
          <div className="loginPage">
            <label htmlFor="username">Username: </label>
            <input
              value={loginInfo.username}
              id="username"
              name="username"
              onChange={handleLoginChange}
            />
          </div>
          <div className="loginPage">
            <label htmlFor="password">Password: </label>
            <input
              value={loginInfo.password}
              type="password"
              id="password"
              name="password"
              onChange={handleLoginChange}
            />
            <div>
              <input className="button" type="submit" value="Login" />
            </div>
          </div>
        </form>
        <p className="font">
          Don't have an account? <Link to="/sign_up" className="links">Sign Up</Link>
        </p>
      </div>
    </main>
  );
}
export default Login;