import React from 'react'

function ProductCard(props) {
  return (
    <div className='border py-5 border-white rounded w-100 text-center'>
         <div className="w-100">
              <img src={props.product.image} className='mx-auto w-70 h-70 rounded-full' alt="" />
         </div>
         <div className="text-content p-10">
             <h2 className='text-3xl'>{props.product.name}</h2>
        <p>Price:{props.product.price}</p>
        <div className="border-1 border-white"></div>
        <p>{props.product.description}</p>
         </div>
    </div>
  )
}

export default ProductCard