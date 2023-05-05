import React,{useState, useEffect} from 'react'
import Listitem from '../components/Listitem'
const Pharmcy = () => {

    let [pharmcy, setPharmcy] = useState([])
    useEffect(()=> {
            getPharmcy()
                },[])
    let getPharmcy = async ()=> {
        let response = await fetch('/pharmacy')
        let data = await response.json()
        setPharmcy(data)
    }
  return (
    <div>
        <div className='pharmacy-list'>
            {pharmcy.map((pharmcy, index) =>(
              <Listitem key={index} pharmcy={pharmcy}/>
            ))}
        </div>
    </div>
  )
}

export default Pharmcy
