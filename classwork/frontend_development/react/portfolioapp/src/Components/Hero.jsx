import React from 'react'
import person from '../assets/dev.png'
import './hero.css'

function Hero() {
  return (
    <div className='px-20 bg-blue-100 text-black'>
        <div className="row flex md:flex-row flex-col justify-around py-20 items-center">
             <div className="text-div animate-slide-right flex flex-col gap-4 md:order-1 order-2">
            <h1 className='text-6xl'>Dev Ratnani</h1>
            <h2 className='text-3xl'>Full Stack Developer</h2>
            <p>Full-stack developer with a passion for turning code into seamless user experiences!</p>
            <div>
                <button className='bg-yellow-300 py-5 px-10 rounded-full'>Download CV</button>
            </div>
        </div>
        <div className="img-div  md:order-2 order-1 animate-slide-right ">
            
            <img src={person} alt="" className='w-70 h-70 rounded-full object-cover '   />
        </div>
        </div>
    </div>
  )
}

export default Hero