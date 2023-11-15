import React from 'react';

const WorkItem = ({ year, title, duration, type, details }) => {
  const styles = {
    container: 'flex flex-col md:flex-row relative border-l border-red-500',
    marker: 'absolute w-3 h-3 bg-red-500 round-full mt-1.5 -left-1.5 border-white',
    info: 'mb-10 ml-4',
    infoText: 'flex flex-wrap gap-4 flex-row items-center justify-start text-xs md:text-sm',
    yearTag: 'incline-block px-2 py-1 font-semibold text-green-300 bg-black rounded-md',
    titleText: 'text-xl font-semibold text-green-300',
    durationTypeText: 'my-1 text-sm font-normal leading-none text-green-300',
    detailsText: 'my-2 text-base text-left font-normal text-green-600',
  };

  return (
    <ol className={styles.container}>
      <li className={styles.info}>
        <div className={styles.marker} />
        <p className={styles.infoText}>
          <span className={styles.yearTag}>{year}</span>
          <span className={styles.titleText}>{title}</span>
          <span className={styles.durationTypeText}>{duration}</span>
          <span className={styles.durationTypeText}>{type}</span>
        </p>
        <p className={styles.detailsText}>{details}</p>
      </li>
    </ol>
  );
};

export default WorkItem;
