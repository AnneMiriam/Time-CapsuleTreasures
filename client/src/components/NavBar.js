import { NavLink, useNavigate } from "react-router-dom";
import React, { useContext, useEffect } from "react";
import { AuthContext } from "./AuthContext";
import "../styles.css"

function LoggedInLinks() {
  const { setUser } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    navigate('/login');
  }, [navigate])

  const handleLogout = () => {
    fetch('/logout', {method: "DELETE"})
    .then(() => {
      setUser(null);
      localStorage.removeItem('user');
      navigate('/login');
    })
  }
  return (
    <nav>
      <NavLink
        to="/"
        className="nav-link homeLink"
        activeClassName="active">
        {/* 🏰 */}
      </NavLink>

      <NavLink
        to="/api/collections"
        className="nav-link collectionLink"
        activeClassName="active">
        🎠 My Collections
      </NavLink>

      <NavLink
        to="/login"
        className="nav-link logoutLink"
        activeClassName="active"
        onClick={handleLogout}>
        Logout
      </NavLink>
    </nav>
  )
}

function LoggedOutLinks() {
  return (
    <nav>
      <NavLink
        to="/login"
        className="nav-link loginLink"
        activeClassName="active">
          {/* <img src="client/src/assets/Login.jpeg" alt="Login" /> */}
      </NavLink>

      <NavLink
        to="/sign_up"
        className="nav-link signupLink"
        activeClassName="active">
        {/* <img src="client/src/assets/Signup.jpeg" alt="Signup" /> */}
      </NavLink>
    </nav>
  )
}

/* define the NavBar component */
function NavBar() {
  const { user } = useContext(AuthContext);
  const loggedIn = user && Object.keys(user).length > 0;
  return (
    <nav>
      <div>
        <ul>
          {loggedIn ? <LoggedInLinks /> : <LoggedOutLinks />}
        </ul>
      </div>
      
    </nav>
  );
}

export default NavBar;