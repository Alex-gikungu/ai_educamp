import React from 'react';

const Leaderboard = ({ topStories }) => {
  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {topStories.map((story, index) => (
          <li key={index}>
            <p>{story.prompt}</p>
            <p>{story.story}</p>
            <p>Upvotes: {story.upvotes}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
