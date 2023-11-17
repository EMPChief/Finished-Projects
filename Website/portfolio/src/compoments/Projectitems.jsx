import React from 'react';

function ProjectItems({ img, title, link, description }) {
  const styles = {
    container: 'relative flex items-center justify-center h-auto w-full shadow-xl shadow-green-300 rounded-xl group hover:bg-gradient-to-r from-stone-800',
    image: 'rounded-xl group-hover:opacity-10',
    infoContainer: 'hidden group-hover:flex flex-col items-center absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center',
    title: 'text-2xl font-bold text-green-600 tracking-wider',
    category: 'pb-4 pt-2 text-green-600',
    link: 'p-3 rounded-lg bg-blue-700 text-green-400 font-bold cursor-pointer text-lg',
  };

  return (
    <div className={styles.container}>
      <img src={img} alt={title} className={styles.image} />
      <div className={styles.infoContainer}>
        <h3 className={styles.title}>{title}</h3>
        <p className={styles.category}>{description}</p>
        <a href={link} target="_blank" rel="noopener noreferrer">
          <p className={styles.link}>
            More info here...
          </p>
        </a>
      </div>
    </div>
  );
}

export default ProjectItems;
