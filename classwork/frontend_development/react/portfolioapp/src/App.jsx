import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import Navbar from './Components/Navbar'
import Hero from './Components/Hero'
import products from './Components/db'
import ProductCard from './Components/ProductCard'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className='bg-gray-900'>
          <header>
                <Navbar/>
          </header>
          <Hero/>
         {/* <div className="flex text-white p-20 justify-between">
               {
             products && products.map((index,i)=>(
                 <ProductCard key={i} product={index}/>
             ))
          }
         </div> */}

      </div>
    </>
  )
}

export default App
