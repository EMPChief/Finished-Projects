import React from 'react';
import ProjectItems from './Projectitems';
import numbercounter from '../assets/numbercounter.png';
import randomiser from '../assets/randomiser.png';
import takeinputandreturnavalue from '../assets/takeinputandreturnavalue.png';
import website from '../assets/website.png';

function Projects() {
  return (
    <div id='project' className='max-w-[1040px] m-auto md:pl-20 py-16'>
      <p className='text-4xl font-bold text-green-500 text-center'>
        Projects
      </p>
      <h2 className='text-center py-8 text-green-400'>
        Some of my projects
      </h2>
      <div className='grid sm:grid-cols-2 gap-12'>
        <ProjectItems img={numbercounter} title='Number Counter' />
        <ProjectItems img={randomiser} title='Number Randomiser' />
        <ProjectItems img={takeinputandreturnavalue} title='Takes an input and outputs a text' />
        <ProjectItems img={website} title='Website' />
      </div>
    </div>
  );
}

export default Projects;
