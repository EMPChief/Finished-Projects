import React from "react";
import { FaRegTrashAlt } from "react-icons/fa";

const style = {
  li: "flex justify-between items-center p-2 bg-blue-200 my-2 capitalize",
  liComplete:
    "flex justify-between bg-blue-400 items-center p-2 my-2 capitalize",
  row: "flex",
  text: "ml-2 cursor-pointer",
  textComplete: "ml-2 cursor-pointer line-through",
  button: "cursor-pointer flex item-center",
};

const Todo = ({ todo, toggleComplete, deleteTodo }) => {
  return (
    <li className={todo.completed ? style.liComplete : style.li}>
      <div className={style.row}>
        <input
          onChange={() => toggleComplete(todo)}
          type="checkbox"
          checked={todo.completed}
        />
        <p
          onClick={() => toggleComplete(todo)}
          className={todo.completed ? style.textComplete : style.text}
        >
          {todo.text}
        </p>
      </div>
      <button onClick={() => deleteTodo(todo.id)}>{<FaRegTrashAlt />}</button>
    </li>
  );
};

export default Todo;
