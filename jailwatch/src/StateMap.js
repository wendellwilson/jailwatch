import React, { useState, useEffect } from "react"
import { geoAlbers, geoPath } from "d3-geo"

const projection = geoAlbers().rotate([0, 62, 0]).scale(7000).center([-79, 36]).translate([3850,3100]);

const StateMap = () => {
   const [geographies, setGeographies] = useState([])

   useEffect(() => {
    fetch("/data/nccounties.json")
      .then(response => {
        if (response.status !== 200) {
          console.log(`There was a problem: ${response.status}`)
          return
        }
        response.json().then(statedata => {
          setGeographies(statedata.features)
        })
      })
   }, [])

  return (
    <svg width={ 900 } height={ 450 } viewBox="0 0 900 450">
      <g className="counties">
        {
          geographies.map((d,i) => (
            <path
              key={ `path-${ i }` }
              d={ geoPath().projection(projection)(d) }
              className="county"
              fill={ `rgba(38,50,56,${ 1 / geographies.length * i})` }
              stroke="#FFFFFF"
              strokeWidth={ 0.5 }
            />
          ))
        }
      </g>
    </svg>
  )
}

export default StateMap
