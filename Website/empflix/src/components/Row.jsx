import axios from "axios";
import React, { useState, useEffect } from "react";
import { MdChevronLeft, MdChevronRight } from "react-icons/md";
import Movie from "./Movie";

const styles = {
  title: "text-white text-2xl font-bold mb-4 md:text-xl p-4",
  container: "relative flex items-center group",
  slider:
    "w-full h-full overflow-x-auto whitespace-nowrap snap-type-mandatory scrollbar-hide relative",
  slideItem:
    "w-40 sm:w-48 md:w-60 lg:w-72 inline-block cursor-pointer relative p-2 scroll-snap-align-start",
  scroll1:
    "bg-white left-0 rounded-full absolute opacity-50 hover:opacity-100 cursor-pointer z-10 hidden group-hover:block",
  scroll2:
    "bg-white right-0 rounded-full absolute opacity-50 hover:opacity-100 cursor-pointer z-10 hidden group-hover:block ",
};

const Row = ({ title, fetchURL }) => {
  const [movies, setMovies] = useState([]);
  const [slider, setSlider] = useState(null);

  useEffect(() => {
    axios.get(fetchURL).then((response) => {
      setMovies(response.data.results);
    });
  }, [fetchURL]);

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

  return (
    <>
      <h2 className={styles.title}>{title}</h2>
      <div className={styles.container}>
        <MdChevronLeft
          onClick={slideLeft}
          size={40}
          className={styles.scroll1}
        />
        <div
          id="Slider"
          className={styles.slider}
          ref={(ref) => setSlider(ref)}
        >
          {movies.map((item, id) => (
            <Movie key={id} item={item} />
          ))}
        </div>
        <MdChevronRight
          onClick={slideRight}
          size={40}
          className={styles.scroll2}
        />
      </div>
    </>
  );
};

export default Row;
