import React, { useState, useEffect } from "react"
import { geoAlbers, geoPath } from "d3-geo"

const projection = geoAlbers().rotate([0, 62, 0]).scale(7000).center([-79, 36]).translate([3850,3100]);

const StateMap = () => {
   const [geographies, setGeographies] = useState([])
   const [markers, setMarkers] = useState([])

   useEffect(() => {
    fetch("/map/nc")
      .then(response => {
        if (response.status !== 200) {
          console.log(`There was a problem: ${response.status}`)
          return
        }
        response.json().then(statedata => {
          setGeographies(statedata)
        })
      })
    fetch("/jails/nc")
      .then(response => {
        if (response.status !== 200) {
          console.log(`There was a problem: ${response.status}`)
          return
        }
        response.json().then(jaildata => {
          setMarkers(jaildata)
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
              d={ geoPath().projection(projection)(d.geometry) }
              className="county"
              fill={ `rgba(38,50,56,${ 1 / geographies.length * i})` }
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
              stroke="#FFFFFF"
              className="marker"
            />
          ))
        }
      </g>
    </svg>
  )
}

export default StateMap
