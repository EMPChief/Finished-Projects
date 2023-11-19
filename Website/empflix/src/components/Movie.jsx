import React, { useState } from 'react';
import { FaHeart, FaRegHeart } from 'react-icons/fa';
import { useAuth } from '../context/AuthContext';
import { db } from '../firebase';
import { arrayUnion, doc, updateDoc } from 'firebase/firestore';

const styles = {
  slideItem: 'w-[160px] sm:w-[200px] md:w-[240px] lg:w-[280px] inline-block cursor-pointer relative p-2 scroll-snap-align-start',
  image: 'w-full h-auto block',
  overlay: 'absolute top-0 left-0 w-full h-full hover:bg-black/80 opacity-0 hover:opacity-100 text-white',
  text: 'white-space-normal text-xs md:text-sm font-bold flex justify-center items-center h-full text-center',
  heart: 'absolute top-4 left-4 text-gray-300',
};

const Movie = ({ item }) => {
  const [like, setLike] = useState(false);
  const { user } = useAuth();

  const savedShow = async () => {
    if (user?.email) {
      setLike(!like);
      await updateDoc(doc(db, 'users', `${user?.email}`), {
        savedShows: arrayUnion({
          id: item.id,
          title: item.title,
          img: item.backdrop_path,
        }),
      });
    } else {
      alert('Please log in to save a show');
    }
  };

  return (
    <div className={styles.slideItem}>
      {item?.backdrop_path && (
        <>
          <img className={styles.image} src={`https://tmdb.org/t/p/w500/${item?.backdrop_path}`} alt={item?.title} />
          <div className={styles.overlay}>
            <p className={styles.text}>{item?.title}</p>
            <p onClick={savedShow} className={styles.heart}>
              {like ? <FaHeart /> : <FaRegHeart />}
            </p>
          </div>
        </>
      )}
    </div>
  );
};

export default Movie;
