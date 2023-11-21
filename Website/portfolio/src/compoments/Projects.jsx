import React from 'react';
import ProjectItems from './Projectitems';
import projectonepic from '../assets/snake.png';
import projecttwopic from '../assets/todo.png';
import projectthreepic from '../assets/trialwebsite.png';
import projectfourpic from '../assets/netflix.png';

function Projects() {
  const styles = {
    container: 'max-w-[1040px] m-auto md:pl-20 py-16',
    title: 'text-4xl font-bold text-green-700 text-center',
    subtitle: 'text-center py-8 text-green-700',
    grid: 'grid sm:grid-cols-2 gap-12',
  };

  return (
    <div id='project' className={styles.container}>
      <p className={styles.title}>
        Projects
      </p>
      <h2 className={styles.subtitle}>
        My programming project
      </h2>
      <div className={styles.grid}>
        <ProjectItems img={projectfourpic} title='EMPFLIX' link='https://www.flix.empchief.com/' description='A website that fetch movies from api and connect with database for login, registering and saving movie.' />
        <ProjectItems img={projectonepic} title='Snake Game' link='https://mega.nz/folder/b2wB3LTA#3qZZERxjUA8ggZSzm8hopA' description='A snake game made it python code and saves score in a text file.' />
        <ProjectItems img={projecttwopic} title='Todo List' link='https://todo.empchief.com/' description='A todo list that interact with backend to save, edit, delete and complete object under you find a link for it' />
        <ProjectItems img={projectthreepic} title='Website' link='http://trial.empchief.com/' description='My first page made out off pure css and html with no framework' />
      </div>
    </div>
  );
}

export default Projects;
