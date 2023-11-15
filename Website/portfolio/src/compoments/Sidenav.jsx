import React, { useState } from 'react';
import {
  AiOutlineMenu,
  AiOutlineHome,
  AiOutlineProject,  // <-- The error seems to be related to this line
  AiOutlineMail,
} from 'react-icons/ai';
import {GrProjects} from 'react-icons/gr';
import {BsPerson} from 'react-icons/bs';

function Sidenav() {
  const [nav, setNav] = useState(false);

  const handleNav = () => {
    setNav(!nav);
  };

  return (
    <div>
      <AiOutlineMenu
        onClick={handleNav}
        className="absolute top-4 right-4 z-[99] md:hidden"/>
      {nav ? (
        <div className='fixed w-full h-screen bg-white/90 flex flex-col justify-center items-center z-20'>
          <a onClick={handleNav} href="#main" className="w-[75%] flex justify-center items-center rounded full shadow-lg bg-green-200 shadow-green-600 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200">
            <AiOutlineHome size={20} />
            <span className="pl-4">Home</span>
          </a>
          <a onClick={handleNav} href="#work" className="w-[75%] flex justify-center items-center rounded full shadow-lg bg-green-200 shadow-green-600 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200">
            <GrProjects size={20} />
            <span className="pl-4">Work</span>
          </a>
          <a onClick={handleNav} href="#project" className="w-[75%] flex justify-center items-center rounded full shadow-lg bg-green-200 shadow-green-600 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200">
            <AiOutlineProject size={20} />
            <span className="pl-4">Project</span>
          </a>
          <a onClick={handleNav} href="#resume" className="w-[75%] flex justify-center items-center rounded full shadow-lg bg-green-200 shadow-green-600 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200">
            <BsPerson size={20} />
            <span className="pl-4">Resume</span>
          </a>
          <a onClick={handleNav} href="#contact" className="w-[75%] flex justify-center items-center rounded full shadow-lg bg-green-200 shadow-green-600 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200">
            <AiOutlineMail size={20} />
            <span className="pl-4">Contact</span>
          </a>
        </div>
      ) : (
        ''
      )}
      <div className= "md:block hidden fixed top-[25%] left-0 z-10">
        <div className="flex flex-col">
          <a href="#main" className= "rounded-full shadow-lg bg-green-200 shadow-green-600 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-300">
            <AiOutlineHome size={15} />
            </a>
            <a href="#work" className= "rounded-full shadow-lg bg-green-200 shadow-green-600 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-300">
            <GrProjects size={15} />
            </a>
            <a href="#project" className= "rounded-full shadow-lg bg-green-200 shadow-green-600 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-300">
            <AiOutlineProject size={15} />
            </a>
            <a href="#resume" className= "rounded-full shadow-lg bg-green-200 shadow-green-600 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-300">
            <BsPerson size={15} />
            </a>
            <a href="#contact" className= "rounded-full shadow-lg bg-green-200 shadow-green-600 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-300">
            <AiOutlineMail size={15} />
            </a>

        </div>
      </div>




    </div>
  );
}

export default Sidenav;
