import React, { useState, useEffect } from 'react';
import { AiOutlinePlus } from 'react-icons/ai';
import Todo from './Todo';
import { query, collection, onSnapshot, doc, updateDoc, addDoc, deleteDoc } from 'firebase/firestore';
import { db } from './firebase';

const style = {
  bg: 'h-screen w-screen p-4 bg-gradient-to-r from-stone-500 to-blue-500',
  container: 'bg-red-500 max-w-[500] mx-auto rounded-md p-4 shadow-xl',
  heading: 'text-3xl text-green-400 text-center p-3 mx-auto',  
  form: 'flex justify-between',
  input: 'border p-2 w-full text-xl text-left',
  button: 'border p-4 ml-2 sm:mt-0 bg-blue-500 hover:bg-blue-700 text-white font-bold py rounded-md',
  count: 'text-xl text-green-400 text-center p-2',
  footer: 'border p-2 text-center text-green-600 bg-stone-300'
};

function App() {
  const [todos, setTodos] = useState([]);
  const [input, setinput] = useState('');

  //reads from database
  useEffect(() => {
    const q = query(collection(db, 'todos'));
    const unsubscribe = onSnapshot(q, (querySnapshot) => {
      let todosArr = []
      querySnapshot.forEach((doc) => {
        todosArr.push({...doc.data(), id: doc.id });
      });
      setTodos(todosArr);});

    

    return () => unsubscribe();
  }, []);

//Update database
const toggleComplete = async(todo) => {
  await updateDoc(doc(db, 'todos', todo.id), { completed: ! todo.completed });
}

//create new todo
const createTodo = async(e) => {
  e.preventDefault()
  if(input === '') 
  {alert("Please enter a valid todo")
  return}
  await addDoc(collection(db, 'todos'), { text: input, completed: false });
  setinput('');
}

//delete todo
const deleteTodo = async(id) => {
  await deleteDoc(doc(db, 'todos', id));
}

  return (
    <div className={style.bg}>
      <div className={style.container}>
        <h3 className={style.heading}>To Do App</h3>
        <form onSubmit={createTodo} className={style.form} action="">
          <input value={input} onChange={(e) => setinput(e.target.value)} className={style.input} type="text" placeholder="Add ToDo" />
          <button className={style.button}>
            <AiOutlinePlus size={30} />
          </button>
        </form>
        <ul>
          {todos.map((todo, index) => (
            <Todo key={index} todo={todo} toggleComplete={toggleComplete} deleteTodo={deleteTodo} />
          ))}
        </ul>

        {todos.length < 1 ? null : <p className={style.count}>you have {todos.length} todos</p>}
        <a href="http://bjornmagne.com/"> <p className={style.footer}>© Bjørn-Magne All rights reserved</p> </a>
      </div>
    </div>
  );
}

export default App;
