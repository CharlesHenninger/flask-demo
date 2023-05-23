import { useState, useEffect } from 'react'
import { NavLink } from "react-router-dom";

export function ProductsPage() {
    const [products, setProducts] = useState([] as any[])
    const [pages, setPages] = useState([] as any[])
    const [currentPage, setPage] = useState([] as any[])
    useEffect(() => {
        fetch("http://127.0.0.1:5001/api/products", {
            method: "GET",
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(resp => resp.json())
            .then(resp => {
                setProducts(resp.products)
                setPages(resp.totalPages)
                setPage(resp.currentPage)
            })
            .catch(error => console.log(error))
    }, []);


    return (
        <div className="productsPage">
            <h1>Products</h1>
            <table>
                <thead>
                    <tr>
                        <td>Id</td>
                        <td>Title</td>
                        <td>Type</td>
                        <td>Price</td>
                    </tr>
                </thead>
                <tbody>
                    {products.map(product =>
                        <tr key={product.id}>
                            <td><NavLink to="/product" state={product.id}>{product.id}</NavLink></td>
                            <td>{product.title}</td>
                            <td>{product.listing_type}</td>
                            <td>{product.price}</td>
                        </tr>
                    )}
                </tbody>
                <br></br>
                <p>Imagine page navigation here</p>
            </table>
        </div>
    );
}
export default ProductsPage;