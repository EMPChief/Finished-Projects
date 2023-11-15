import React from 'react';

const Contact = () => {
  return (
    <div id='contact' className='max-w-[1040px] m-auto md:pl-20 p-4 py-16'>
      <h1 className='py-4 text-4xl font-bold text-center text-green-600'>Contact</h1>
      <form action="https://getform.io/f/4838c3be-6106-4e70-a36f-924aa116be55" method="POST" encType='multipart/form-data'>
        <div className='grid md:grid-cols-2 gap-4 w-full py-2'>
          <div className='flex flex-col'>
            <label className='uppercase text-5m py-2'>Name</label>
            <input className='border-2 rounded-lg p-3 flex border-green-300' type='text' name='name' />
          </div>
          <div className='flex flex-col'>
            <label className='uppercase text-5m py-2'>Phone Number</label>
            <input className='border-2 rounded-lg p-3 flex border-green-300' type='tel' name='phone' />
          </div>
          <div className='flex flex-col py-2'>
            <label className='uppercase text-5m py-2'>Email</label>
            <input className='border-2 rounded-lg p-3 flex border-green-300' type='email' name='email' />
          </div>
          <div className='flex flex-col py-2'>
            <label className='uppercase text-5m py-2'>Subject</label>
            <input className='border-2 rounded-lg p-3 flex border-green-300' type='text' name='text' />
          </div>
          <div className='flex flex-col'>
            <label className='uppercase text-5m py-2'>Message</label>
            <textarea  className='border-2 rounded-lg p-3 flex border-green-300'rows='10' name='message'></textarea>
          </div>
        </div>
        <button className='bg-red-600 text-green-200 mt-4 w-full p-4 rounded-lg'>Send Message</button>
      </form>
    </div>
  );
};

export default Contact;
