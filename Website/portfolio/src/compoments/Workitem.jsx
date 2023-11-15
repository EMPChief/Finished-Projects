import React from 'react'

const Workitem = ({year, title, duration, type, details}) => {
  return (
    <ol className='flex flex-col md:flex-row relative border-l border-red-500'>
        <li className='mb-10 ml-4'>
            <div className='absolute w-3 h-3 bg-red-500 round-full mt-1.5 -left-1.5 border-white' />
            <p className='flex flex-wrap gap-4 flex-row item-center justify-start text-xs md:text-sm'>
                <span className='incline-block px-2 py-1 font-semibold text-green-300 bg-black rounded-md'>{year}</span>
                <span className='text-xl  font-semibold text-green-300'>{title}</span>
                <span className='my-1 text-sm font-normal leading-none text-green-300'>{duration}</span>
                <span className='my-1 text-sm font-normal leading-none text-green-300'>{type}</span>
            </p>
            <p className='my-2 text-base text-left font-normal text-green-600'>{details}</p>
        </li>
    </ol>
  )
}

export default Workitem