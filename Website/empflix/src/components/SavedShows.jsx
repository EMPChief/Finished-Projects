import React, { useState, useEffect } from "react";
import { MdChevronLeft, MdChevronRight } from "react-icons/md";
import { useAuth } from "../context/AuthContext";
import { db } from "../firebase";
import { updateDoc, doc, onSnapshot } from "firebase/firestore";
import { AiOutlineClose } from "react-icons/ai";

const styles = {
  title:
    "text-white text-2xl font-bold mb-4 md:text-xl p-4 text-center absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity duration-300",
  container: "relative flex flex-col items-start group overflow-hidden",
  slider:
    "w-full h-full overflow-x-auto whitespace-nowrap snap-type-mandatory scrollbar-hide relative",
  slideItemMovie:
    "w-[160px] sm:w-[200px] md:w-[240px] lg:w-[280px] inline-block relative p-2 scroll-snap-align-start overflow-hidden mb-4 group",
  imageContainer: "relative",
  image: "w-full h-auto block",
  overlay:
    "absolute bottom-0 left-0 w-full h-1/3 bg-gradient-to-t from-black to-transparent opacity-0 group-hover:opacity-100 text-white transition-opacity duration-300",
  text: "white-space-normal text-xs md:text-sm font-bold flex justify-center items-center h-full text-center",
  trash:
    "absolute text-gray-300 top-4 left-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300 cursor-pointer",
  arrow:
    "z-10 rounded-full opacity-0 group-hover:opacity-100 cursor-pointer hover:opacity-100 transition-opacity duration-300",
};

const SavedShows = () => {
  const { user } = useAuth();
  const [movies, setMovies] = useState([]);
  const [slider, setSlider] = useState();

  const slideLeft = () => {
    if (slider) {
      slider.scrollLeft -= 500;
    }
  };

  const slideRight = () => {
    if (slider) {
      slider.scrollLeft += 500;
    }
  };

  useEffect(() => {
    onSnapshot(doc(db, "users", `${user?.email}`), (doc) => {
      setMovies(doc.data()?.savedShows || []);
    });
  }, [user?.email]);

  const movieRef = doc(db, "users", `${user?.email}`);
  const deleteShow = async (passedID) => {
    try {
      const result = movies.filter((item) => item.id !== passedID);
      await updateDoc(movieRef, {
        savedShows: result,
      });
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.slider} ref={(ref) => setSlider(ref)}>
        {movies.map((item, id) => (
          <div className={styles.slideItemMovie} key={id}>
            <div className={styles.imageContainer}>
              {item?.img && (
                <img
                  className={styles.image}
                  src={`https://tmdb.org/t/p/w500/${item?.img}`}
                  alt={item?.title}
                />
              )}
              <div className={styles.overlay}>
                <p className={styles.text}>{item?.title}</p>
                <p className={styles.trash} onClick={() => deleteShow(item.id)}>
                  <AiOutlineClose />
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
      <div className={`flex justify-between w-full ${styles.arrow}`}>
        <MdChevronLeft
          onClick={slideLeft}
          size={40}
          className="z-10 bg-white rounded-full opacity-50 hover:opacity-100"
        />
        <MdChevronRight
          onClick={slideRight}
          size={40}
          className="z-10 bg-white rounded-full opacity-50 hover:opacity-100"
        />
      </div>
    </div>
  );
};

export default SavedShows;
