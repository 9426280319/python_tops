import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Trendingsong from './componets/Trendingsong'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <h1>Welcome to My React Zomato App</h1>
      <Trendingsong />
    </div>
  )
}

export default App
