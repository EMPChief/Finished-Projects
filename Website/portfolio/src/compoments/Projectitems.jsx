import React from 'react';

function ProjectItems({ img, title }) {
  return (
    <div className='relative flex items-center justify-center h-auto w-full shadow-xl shadow-green-300 rounded-xl group hover:bg-gradient-to-r from-red-600'>
      <img src={img} alt={title} className='rounded-xl group-hover:opacity-10' />
      <div className='hidden group-hover:flex flex-col items-center absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center'>
        <h3 className='text-2xl font-bold text-blue-400 tracking-wider'>
          {title}
        </h3>
        <p className='pb-4 pt-2 text-blue-400'>Projects</p>
        <a href="">
          <p className='p-3 rounded-lg bg-green-500 text-blue-400 font-bold cursor-pointer text-lg'>
            More info here...
          </p>
        </a>
      </div>
    </div>
  );
}

export default ProjectItems;
