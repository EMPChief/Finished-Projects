import React, { useState, useEffect } from "react";
import axios from "axios";
import requests from "../requests";

const styles = {
  mainContainer: "relative w-full h-[550px] text-white",
  contentContainer: "relative w-full h-full",
  backgroundImageOverlay:
    "absolute w-full h-full bg-gradient-to-r from-black opacity-60",
  movieImage: "w-full h-full object-cover",
  containEverything:
    "absolute inset-0 flex flex-col justify-center items-left p-4 md:p-8",
  buttonContainer: "flex my-4",
  playButton: "border bg-gray-300 text-black border-gray-300 py-2 px-5",
  watchLaterButton: "border text-white border-gray-300 py-2 px-5 ml-4",
  title: "text-3xl md:text-5xl text-white font-bold",
  releaseDate: "text-gray-400 text-sm",
  overview: "w-full md:max-w-[70%] lg:max-w-[50%] xl:max-w-[35%] text-gray-100",
};

const Main = () => {
  const [movies, setMovies] = useState([]);
  const movie = movies[Math.floor(Math.random() * movies.length)];

  useEffect(() => {
    axios.get(requests.RequestPopular).then((response) => {
      setMovies(response.data.results);
    });
  }, []);
  const truncateString = (str, num) => {
    if (str?.length > num) {
      return str.slice(0, num) + "...";
    } else {
      return str;
    }
  };

  return (
    <div className={styles.mainContainer}>
      <div className={styles.contentContainer}>
        <div className={styles.backgroundImageOverlay}></div>
        <img
          className={styles.movieImage}
          src={`https://tmdb.org/t/p/original/${movie?.backdrop_path}`}
          alt={movie?.title}
        />
        <div className={styles.containEverything}>
          <h1 className={styles.title}>{movie?.title}</h1>
          <div className={styles.buttonContainer}>
            <button className={styles.playButton}>Play</button>
            <button className={styles.watchLaterButton}>Watch Later</button>
          </div>
          <p className={styles.releaseDate}>Released: {movie?.release_date}</p>
          <p className={styles.overview}>
            {truncateString(movie?.overview, 150)}
          </p>
        </div>
      </div>
    </div>
  );
};

export default Main;
