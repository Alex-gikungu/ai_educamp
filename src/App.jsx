import React, { useState } from 'react';
import StoryForm from './components/StoryForm';
import GeneratedStory from './components/GeneratedStory';

const App = () => {
  const [generatedStory, setGeneratedStory] = useState('');

  const handleGenerateStory = async (prompt) => {
    try {
      const response = await fetch('http://localhost:3000/api/generate-story', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt })
      });

      if (response.ok) {
        const data = await response.json();
        setGeneratedStory(data.story);
      } else {
        console.error('Failed to generate story:', response.statusText);
      }
    } catch (error) {
      console.error('Error generating story:', error);
    }
  };

  return (
    <div>
      <h1>Story Generator</h1>
      <StoryForm onGenerateStory={handleGenerateStory} />
      {generatedStory && <GeneratedStory story={generatedStory} />}
    </div>
  );
};

export default App;
