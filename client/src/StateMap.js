import React, { useState, useEffect } from "react"
// import { ComposableMap, Geographies, Geography, Marker } from "react-simple-maps"
import { geoAlbers, geoPath } from "d3-geo"
import Api from "./helper/api";



const StateMap = () => {
   const [regions, setRegions] = useState([])
   const [markers, setMarkers] = useState([])

   useEffect(() => {
    const api = new Api();
    api
      .getCountiesList("NC")
      .then(response => {
        if (response.status !== 200) {
          console.log(`There was a problem: ${response.status}`)
          return
        }
        setRegions(response.data)
      })
    api
      .getJailsList("NC")
      .then(response => {
        if (response.status !== 200) {
          console.log(`There was a problem: ${response.status}`)
          return
        }
          setMarkers(response.data)
      })
   }, [])

  if (!regions || !markers) {
    return <div>Loading...</div>;
  }

  const projection = geoAlbers().rotate([0, 62, 0]).scale(7200).center([-79, 36]).translate([3980,3150]);
  // const projection = geoAlbersUsa();

  return (
    <svg width={ 960 } height={ 600 }>
      <g className="counties">
        {
          regions.map((d,i) => (
            <path
              key={ `path-${ i }` }
              d={ geoPath().projection(projection)(d.geometry) }
              className="county"
              fill={ `rgba(38,50,56,${ 1 / regions.length * i})` }
              name={d.name}
              stroke="#FFFFFF"
              strokeWidth={ 0.5 }
            />
          ))
        }
      </g>
      <g className="markers">
        {
          markers.map((jail, i) => (
            <circle
              key={ `marker-${i}` }
              cx={ projection(jail.location.coordinates)[0] }
              cy={ projection(jail.location.coordinates)[1] }
              r={ 2 }
              fill="#E91E63"
              className="marker"
            />
          ))
        }
      </g>
    </svg>
  );
};

export default StateMap
