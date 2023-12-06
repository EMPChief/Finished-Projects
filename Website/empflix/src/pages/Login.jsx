import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const styles = {
  container: "w-full h-screen",
  background: "hidden sm:block absolute w-full h-full object-cover",
  overlay: "bg-black fixed top-0 left-0 w-full h-screen opacity-60",
  login: "fixed w-full px-4 py-24 z-50",
  loginform: "max-w-[500px] h-[700px] mx-auto bg-black/75 text-white",
  formContainer: "max-w-[350px] mx-auto py-16",
  title: "text-4xl font-bold mb-6",
  emailInput:
    "bg-green-200 text-blue-700 rounded w-full p-2 mb-4 bg-transparent border-b border-white focus:outline-none",
  passwordInput:
    "bg-green-200 rounded text-blue-700 w-full p-2 mb-4 bg-transparent border-b border-white focus:outline-none",
  checkboxContainer: "flex items-center mb-4 text-white",
  checkbox: "mr-2",
  rememberMeLink: "text-sm text-blue-500 hover:underline cursor-pointer",
  loginButton:
    "w-full p-2 bg-red-600 rounded text-white hover:bg-red-700 cursor-pointer",
  needHelpLink: "text-blue-500 hover:underline cursor-pointer",
  signupLink: "text-red-500 hover:underline cursor-pointer",
  notSubscribedText: "text-blue-500",
  errorText: "text-red-500 mb-4",
};

const Login = () => {
  const { logIn } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await logIn(email, password);
      navigate("/");
    } catch (error) {
      setError("Invalid email or password.");
    }
  };

  return (
    <div className={styles.container}>
      <img
        className={styles.background}
        src="https://trial.empchief.com/pictures/IMG_4281.JPG"
        alt="Background"
      />
      <div className={styles.overlay}></div>
      <div className={styles.login}>
        <div className={styles.loginform}>
          <div className={styles.formContainer}>
            <h1 className={styles.title}>Login</h1>
            <form onSubmit={handleSubmit}>
              <input
                className={styles.emailInput}
                type="email"
                placeholder="Email"
                autoComplete="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
              <input
                className={styles.passwordInput}
                type="password"
                placeholder="Password"
                autoComplete="current-password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <div className={styles.checkboxContainer}>
                <label className={styles.checkbox}>
                  <input type="checkbox" />
                </label>
                <p className={styles.rememberMeLink}>Remember me</p>
              </div>
              <button type="submit" className={styles.loginButton}>
                Login
              </button>
              {error && <p className={styles.errorText}>{error}</p>}
              <p className={styles.needHelpLink}>Need help?</p>
              <p className={styles.notSubscribedText}>
                Not subscribed yet?{" "}
                <Link to="/Signup" className={styles.signupLink}>
                  Sign up
                </Link>
              </p>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
