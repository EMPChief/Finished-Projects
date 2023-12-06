import React, { useState } from "react";
import {
  AiOutlineMenu,
  AiOutlineHome,
  AiOutlineProject,
  AiOutlineMail,
} from "react-icons/ai";
import { GrProjects } from "react-icons/gr";
import { BsPerson } from "react-icons/bs";

function Sidenav() {
  const [nav, setNav] = useState(false);

  const handleNav = () => {
    setNav(!nav);
  };
  const styles = {
    menuIcon: "absolute top-4 right-4 z-[99] md:hidden",
    navContainer:
      "fixed w-full h-screen bg-white/90 flex flex-col justify-center items-center z-20",
    navLink:
      "w-[75%] flex justify-center items-center rounded-full shadow-lg bg-green-200 shadow-green-600 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200",
    icon: "size={20}",
    linkText: "pl-4",
    sideNav: "md:block hidden fixed top-[25%] left-0 z-10",
  };

  return (
    <div>
      <AiOutlineMenu onClick={handleNav} className={styles.menuIcon} />
      {nav ? (
        <div className={styles.navContainer}>
          <a onClick={handleNav} href="#main" className={styles.navLink}>
            <AiOutlineHome size={20} />
            <span className={styles.linkText}>Home</span>
          </a>
          <a onClick={handleNav} href="#work" className={styles.navLink}>
            <GrProjects size={20} />
            <span className={styles.linkText}>Work</span>
          </a>
          <a onClick={handleNav} href="#project" className={styles.navLink}>
            <AiOutlineProject size={20} />
            <span className={styles.linkText}>Project</span>
          </a>
          <a onClick={handleNav} href="#resume" className={styles.navLink}>
            <BsPerson size={20} />
            <span className={styles.linkText}>Resume</span>
          </a>
          <a onClick={handleNav} href="#contact" className={styles.navLink}>
            <AiOutlineMail size={20} />
            <span className={styles.linkText}>Contact</span>
          </a>
        </div>
      ) : (
        ""
      )}
      <div className={styles.sideNav}>
        <div className="flex flex-col">
          <a href="#main" className={styles.navLink}>
            <AiOutlineHome size={15} />
          </a>
          <a href="#work" className={styles.navLink}>
            <GrProjects size={15} />
          </a>
          <a href="#project" className={styles.navLink}>
            <AiOutlineProject size={15} />
          </a>
          <a href="#resume" className={styles.navLink}>
            <BsPerson size={15} />
          </a>
          <a href="#contact" className={styles.navLink}>
            <AiOutlineMail size={15} />
          </a>
        </div>
      </div>
    </div>
  );
}

export default Sidenav;
