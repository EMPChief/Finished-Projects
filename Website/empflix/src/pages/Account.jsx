import React from 'react';
import SavedShows from '../components/SavedShows';

const styles = {
  container: 'relative',
  background: 'w-full h-[400px] object-cover',
  overlay: 'bg-black/60 fixed top-0 left-0 w-full h-[550px]',
  content: 'absolute top-[20%] left-0 transform p-4 md:p-8 text-white',
  title: 'text-4xl md:text-7xl font-bold text-green-400',
};

const Account = () => {
  return (
    <div className={styles.container}>
      <img className={styles.background} src="https://trial.empchief.com/pictures/IMG_4281.JPG" alt="Background" />
      <div className={styles.overlay}></div>
      <div className={styles.content}>
        <h1 className={styles.title}>My Shows</h1>
      </div>
      <SavedShows />
    </div>
  );
};

export default Account;
