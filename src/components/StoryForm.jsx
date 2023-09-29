import React, { useState } from "react";
import axios from "axios";

const StoryGenerator = () => {
  const [prompt, setPrompt] = useState("");
  const [story, setStory] = useState("");

  const generateStory = async () => {
    const response = await axios.post("/story", {
      prompt,
    });

    const generatedStory = response.data.story;

    setStory(generatedStory);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter a prompt..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button onClick={generateStory}>Generate Story</button>
      <p>{story}</p>
    </div>
  );
};

export default StoryGenerator;
