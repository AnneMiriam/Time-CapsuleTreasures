import React from "react";
import { useEffect, useState } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes
} from "react-router-dom"; 
import Login from "../pages/Login";
import Home from "../pages/Home";
import Signup from "../pages/Signup";
import Collection from "../pages/Collection";
import User from "../pages/User"
import NavBar from "./NavBar";
import { AuthProvider } from "./AuthContext";

const App = () => {
    return(
        <Router>

            <AuthProvider>
                <>
                    <NavBar />
                </>
                <div>
                    <Routes>
                        <Route path='/' element={<Home />} />
                        <Route path="/login" element={<Login />} />
                        <Route path="/sign_up" element={<Signup />} />
                        <Route path="/user" element={<User />} />
                        <Route path="/collections" element={<Collection />} />
                    </Routes>
                </div>
            </AuthProvider>
        </Router>
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