import React, { useContext, useEffect } from "react";
// import { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import Login from "../pages/Login";
import Home from "../pages/Home";
import UserHome from "../pages/UserHome";
import Signup from "../pages/Signup";
import Collection from "../pages/Collection";
import User from "../pages/User";
import NavBar from "./NavBar";
import { AuthContext } from "./AuthContext";

const App = () => {
  const { user, setUser } = useContext(AuthContext);

  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((data) => setUser(data));
      } else {
        setUser(null);
      }
    });
  }, []);

  if (user === null) {
    // navigate to login
  }

  if (user === undefined) {
    return;
  }

  return (
    <>
      <NavBar />

      <div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/sign_up" element={<Signup />} />
          <Route path="/user_home" element={<UserHome />} />
          <Route path="/collections" element={<User />} />
          <Route path="/collections/:id" element={<Collection />} />
        </Routes>
      </div>
    </>
  );
};
export default App;
