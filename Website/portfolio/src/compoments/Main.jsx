import React from 'react';
import { TypeAnimation } from 'react-type-animation';
import { FaFacebookF } from 'react-icons/fa';
import galaxy from '../assets/Galaxy-Floating.png';

const Main = () => {
  return (
    <div id='main'>
      <img
        className='w-full h-screen object-cover object-left scale-x-[1]'
        src={galaxy}
        alt='Background'
      />
      <div className='w-full h-screen absolute inset-0 flex flex-col justify-center items-center bg-white/20'>
        <div className="max-w-[700px] mx-auto h-full w-full flex flex-col justify-center lg:items-start items-center text-center">
          <h1 className='sm:text-5xl text-4xl font-bold text-green-500'>Eg er Bjørn-Magne </h1>
          <h2 className="flex sm:text-3xl text-xl text-green-500">
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
              style={{
                fontSize: '1em',
                display: 'inline-block',
                paddingLeft: '4px',
              }}
              repeat={Infinity}
            />
          </h2>
          <div className='flex justify-between pt-6 max-w-[200px] w-full'>
            <FaFacebookF />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Main;
