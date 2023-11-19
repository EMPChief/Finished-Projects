const key = import.meta.env.VITE_REACT_APP_IMDB_API_KEY;

const requests = {
  RequestPopular: `https://api.themoviedb.org/3/movie/popular?api_key=${key}&language=en-US&page=1`,
  RequestTopRated: `https://api.themoviedb.org/3/movie/top_rated?api_key=${key}&language=en-US&page=1`,
  RequestTrending: `https://api.themoviedb.org/3/trending/all/day?api_key=${key}`,
  RequestHorror: `https://api.themoviedb.org/3/search/movie?api_key=${key}&language=en-US&query=horror&page=1&include_adult=false`,
  RequestActionMovies: `https://api.themoviedb.org/3/discover/movie?api_key=${key}&with_genres=28`,
  RequestUpcoming: `https://api.themoviedb.org/3/movie/upcoming?api_key=${key}&language=en-US&page=1`,
  RequestComedyMovies: `https://api.themoviedb.org/3/discover/movie?api_key=${key}&with_genres=35`,
  RequestKDramas: `https://api.themoviedb.org/3/discover/tv?api_key=${key}&with_genres=18&region=KR`,
  RequestCDramas: `https://api.themoviedb.org/3/discover/tv?api_key=${key}&with_genres=18&region=CN`,
};

export default requests;
