import React from 'react';
import { TypeAnimation } from 'react-type-animation';
import { FaFacebookF } from 'react-icons/fa';
import Lovund from '../assets/IMG_4281.png';

const Main = () => {
  const styles = {
    mainContainer: 'w-full h-screen absolute inset-0 flex flex-col justify-center items-center bg-white/50',
    contentContainer: 'max-w-[700px] mx-auto h-full w-full flex flex-col justify-center lg:items-start items-center text-center',
    title: 'sm:text-5xl text-4xl font-bold text-green-500',
    subTitle: 'flex sm:text-3xl text-xl text-green-500',
    typeAnimation: {
      fontSize: '1em',
      display: 'inline-block',
      paddingLeft: '4px',
    },
    socialIconContainer: 'flex justify-between pt-6 max-w-[200px] w-full',
  };

  return (
    <div id='main'>
      <img
        className='w-full h-screen object-cover object-left scale-x-[1]'
        src={Lovund}
        alt='Background'
      />
      <div className={styles.mainContainer}>
        <div className={styles.contentContainer}>
          <h1 className={styles.title}>Eg er Bjørn-Magne </h1>
          <h2 className={styles.subTitle}>
            Eg er{' '}
            <TypeAnimation
              sequence={[
                'Programmerer',
                1000,
                'Fotograf',
                1000,
                'Teknisk Entusiast',
                1000,
                'Jobb Dreven',
                1000,
              ]}
              wrapper='span'
              cursor={true}
              style={styles.typeAnimation}
              repeat={Infinity}
            />
          </h2>
          <div className={styles.socialIconContainer}>
            <FaFacebookF />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Main;
