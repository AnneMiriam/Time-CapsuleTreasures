import React from "react";
import { useEffect, useState } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes
} from "react-router-dom"; //KLP added Navigate
import Login from "../pages/Login";
import Home from "../pages/Home";
import Signup from "../pages/Signup";
// import User from "../pages/User"
// import LogoutButton from "../components/LogoutButton";
import { AuthProvider } from "./AuthContext";

const App = () => {
    return(
        <AuthProvider>
            <Router>
                <Routes>
                    <Route path='/' element={<Home />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/sign_up" element={<Signup />} />
                    {/* <Route path="/user" element={<User />} /> */}
                    {/* <Route path="/collections" element={<Collections />} /> */}
                </Routes>
            </Router>
        </AuthProvider>
    );
};
export default App;
//   const [user, setUser] = useState();

//   useEffect(() => {
//     fetch("/check_session")
//       .then((r) => r.json())
//       .then((data) => {
//         if (data.id) {
//           setUser(data);
//         } else {
//           setUser(null);
//         }
//       });
//   }, []);

//   return (

//     <Router>
//       {user && <LogoutButton setUser={setUser} />}{" "}
//       {/* Render LogoutButton if user is logged in */}
//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route
//           path="/login"
//           element={
//             !user ? <Login setUser={setUser} /> : <Navigate to="/user" />
//           }
//         />
//         <Route
//           path="/sign_up"
//           element={
//             !user ? <Signup setUser={setUser} /> : <Navigate to="/user" />
//           }
//         />
//         <Route
//           path="/user"
//           element={user ? <User /> : <Navigate to="/login" />}
//         />
//         <Route
//           path="/collections"
//           element={user ? <Trips /> : <Navigate to="/login" />}
//         />
//         {/* Add other routes as needed */}
//       </Routes>
//     </Router>
//   );
// };
// export default App;