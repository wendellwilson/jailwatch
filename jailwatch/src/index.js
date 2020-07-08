import React from "react";
import ReactDOM from "react-dom";

import "./styles.css";

import StateMap from "./StateMap";

function App() {
  return (
    <div>
      <StateMap />
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
