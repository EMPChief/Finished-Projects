import React from 'react';
import ProjectItems from './Projectitems';
import numberCounter from '../assets/numbercounter.png';
import randomiser from '../assets/randomiser.png';
import Todo from '../assets/Todo.png';
import website from '../assets/website.png';

function Projects() {
  const styles = {
    container: 'max-w-[1040px] m-auto md:pl-20 py-16',
    title: 'text-4xl font-bold text-green-500 text-center',
    subtitle: 'text-center py-8 text-green-400',
    grid: 'grid sm:grid-cols-2 gap-12',
  };

  return (
    <div id='project' className={styles.container}>
      <p className={styles.title}>
        Projects
      </p>
      <h2 className={styles.subtitle}>
        Some of my projects
      </h2>
      <div className={styles.grid}>
        <ProjectItems img={numberCounter} title='Number Counter' link='home' description='A project that counts numbers.' />
        <ProjectItems img={randomiser} title='Number Randomiser' link='/home' description='A project that counts numbers.' />
        <ProjectItems img={Todo} title='Todo List' link='https://todo.empchief.com/' description='Its a working todo list with backend' />
        <ProjectItems img={website} title='Website' link='/home' description='A project that counts numbers.' />
      </div>
    </div>
  );
}

export default Projects;
