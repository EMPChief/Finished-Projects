import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const style = {
  title: 'text-red-600 text-4xl font-bold cursor-pointer',
  button: 'text-white pr-4',
  buttonPrimary: 'bg-red-600 px-6 py-2 rounded cursor-pointer text-white mx-2',
  firstdiv: 'flex items-center justify-between p-4 z-[100] w-full absolute',
};

const Navbar = () => {
  const { user, logOut } = useAuth();
  const navigate = useNavigate()
  const handleLogout = async () => {
    try {
      await logOut();
      navigate('/');
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className={style.firstdiv}>
      <Link to='/'>
        <h1 className={style.title}>EMPFLIX</h1>
      </Link>
      <div>
        {user ? (
          <>
            <Link to='/Account'>
              <button className={style.button}>Account</button>
            </Link>
            <button className={style.buttonPrimary} onClick={handleLogout}>
              Logout
            </button>
          </>
        ) : (
          <>
            <Link to='/Login'>
              <button className={style.button}>Sign In</button>
            </Link>
            <Link to='/Signup'>
              <button className={style.buttonPrimary}>Sign Up</button>
            </Link>
          </>
        )}
      </div>
    </div>
  );
};

export default Navbar;
