import React, { useState } from "react";
import Sidenav from "./compoments/Sidenav";
import Main from "./compoments/Main";
import Work from "./compoments/Work";
import Projects from "./compoments/Projects";
import Contact from "./compoments/Contact";

function App() {
  return (
    <div>
      <Sidenav />
      <Main />
      <Work />
      <Projects />
      <Contact />
    </div>
  );
}

export default App;
