import React from 'react'

function Navbar() {
  return (
    <div className='text-white bg-blue-800 py-5 flex  px-20 md:flex gap-4  md:flex-row flex-col justify-between  items-center' >
        <div className="logodiv " >
                <label htmlFor="" className='text-3xl font-bold'>Dev Ratnani</label>
        </div>
        <div>
            <ul className='flex flex-col md:flex-row text-2xl gap-4' >
                <li className="border-b md:w-auto w-100 text-center border-gray-600 py-3 md:border-0"><a href="">Home</a></li>
                <li className="border-b md:w-auto w-100 text-center border-gray-600 py-3 md:border-0"><a href="">About</a></li>
                <li className="border-b md:w-auto w-100 text-center border-gray-600 py-3 md:border-0"><a href="">Contact</a></li>
                <li className="border-b md:w-auto w-100 text-center border-gray-600 py-3 md:border-0"><a href="">Project</a></li>
                
            </ul>
        </div>
        <div>
            <button  className='bg-black-500 py-5 px-10'>Change Theme</button>
        </div>
    </div>
    
  )
}

export default Navbar