import React from 'react';
import Main from '../components/Main';
import Row from '../components/Row';
import requests from '../requests';

const Home = () => {
  return (
    <div>
      <Main />
      <Row title='Popular' fetchURL={requests.RequestPopular} />
      <Row title='Top Rated' fetchURL={requests.RequestTopRated} />
      <Row title='Upcoming' fetchURL={requests.RequestUpcoming} />
      <Row title='Trending' fetchURL={requests.RequestTrending} />
      <Row title='Horror' fetchURL={requests.RequestHorror} />
      <Row title='Action Movie' fetchURL={requests.RequestActionMovies} />
      <Row title='Korean Drama' fetchURL={requests.RequestKDramas} />
      <Row title='Chinese Drama' fetchURL={requests.RequestCDramas} />
    </div>
  );
};

export default Home;
