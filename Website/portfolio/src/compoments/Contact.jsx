import React from 'react';

const Contact = () => {
  const styles = {
    container: 'max-w-[1040px] m-auto md:pl-20 p-4 py-16',
    title: 'py-4 text-4xl font-bold text-center text-green-600',
    formGrid: 'grid md:grid-cols-2 gap-4 w-full py-2',
    inputContainer: 'flex flex-col',
    label: 'uppercase text-5m py-2',
    input: 'border-2 rounded-lg p-3 flex border-green-300',
    button: 'bg-red-600 text-green-200 mt-4 w-full p-4 rounded-lg',
  };

  return (
    <div id='contact' className={styles.container}>
      <h1 className={styles.title}>Contact</h1>
      <form action="https://getform.io/f/4838c3be-6106-4e70-a36f-924aa116be55" method="POST" encType='multipart/form-data'>
        <div className={styles.formGrid}>
          <div className={styles.inputContainer}>
            <label className={styles.label}>Name</label>
            <input className={styles.input} type='text' name='name' />
          </div>
          <div className={styles.inputContainer}>
            <label className={styles.label}>Phone Number</label>
            <input className={styles.input} type='tel' name='phone' />
          </div>
          <div className={`${styles.inputContainer} py-2`}>
            <label className={styles.label}>Email</label>
            <input className={styles.input} type='email' name='email' />
          </div>
          <div className={`${styles.inputContainer} py-2`}>
            <label className={styles.label}>Subject</label>
            <input className={styles.input} type='text' name='text' />
          </div>
          <div className={styles.inputContainer}>
            <label className={styles.label}>Message</label>
            <textarea className={styles.input} rows='10' name='message'></textarea>
          </div>
        </div>
        <button className={styles.button}>Send Message</button>
      </form>
    </div>
  );
};

export default Contact;
