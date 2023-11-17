import React from 'react';
import ProjectItems from './Projectitems';
import numberCounter from '../assets/numbercounter.png';
import Snake from '../assets/SnakeGame.png';
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
        My programming projects
      </h2>
      <div className={styles.grid}>
        <ProjectItems img={numberCounter} title='Snake Game' link='home' description='A project that counts numbers.' />
        <ProjectItems img={Snake} title='Number Randomize' link='https://mega.nz/folder/b2wB3LTA#3qZZERxjUA8ggZSzm8hopA' description='A snake game made it python code and saves score in a text file.' />
        <ProjectItems img={Todo} title='Todo List' link='https://todo.empchief.com/' description='A todo list that interact with backend to save, edit, delete and complete object under you find a link for it' />
        <ProjectItems img={website} title='Website' link='http://trial.empchief.com/' description='My first page made out off pure css and html with no framework' />
      </div>
    </div>
  );
}

export default Projects;
