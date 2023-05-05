import React from 'react'

const PharmcyPagr = ({match}) => {
    let pharmcyId = match.params.id
  return (
    <div>
       <h1>Sigle pharmcy {pharmcyId}</h1>
    </div>
  )
}

export default PharmcyPagr
