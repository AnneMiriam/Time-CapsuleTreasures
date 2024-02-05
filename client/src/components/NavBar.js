import { NavLink, useLocation } from "react-router-dom";
// import "./NavBar.css";
import "../styles.css"

/* define the NavBar component */
function NavBar() {
//   const location = useLocation();

  return (
    <nav>
      <NavLink
        to="/"
        /* add styling to Navlink */
        className="nav-link homeLink"
        activeClassName="active">
        {/* 🏰 */}
      </NavLink>

      <NavLink
        to="/login"
        className="nav-link loginLink"
        activeClassName="active">
        {/* 🪵📥 */}
      </NavLink>

      <NavLink
        to="/sign_up"
        className="nav-link signupLink"
        activeClassName="active">
         {/* 🪧👆🏻 */}
      </NavLink>

      <NavLink
        to="/collections"
        className="nav-link tripLink"
        activeClassName="active">
        {/* 🎠 */}
      </NavLink>
    </nav>
  );
}

export default NavBar;