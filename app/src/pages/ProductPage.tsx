import { useState, useEffect } from 'react'
import { useLocation } from 'react-router-dom';

export function ProductPage() {
    const [orders, setOrders] = useState([] as any[])
    const [title, setTitle] = useState([] as any[])
    const [price, setPrice] = useState([] as any[])
    const [type, setType] = useState([] as any[])
    const [pages, setPages] = useState([] as any[])
    const [currentPage, setPage] = useState([] as any[])
    const [totalRevenue, setRevenue] = useState()
    const { state } = useLocation();

    useEffect(() => {
        fetch('http://127.0.0.1:5001/api/product?productId=' + state, {
            method: "GET",
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(resp => resp.json())
            .then(resp => {
                setTitle(resp.product.title)
                setOrders(resp.orders)
                setPrice(resp.product.price)
                setType(resp.product.listing_type)
                setRevenue(resp.revenue.total)
                setPages(resp.totalPages)
                setPage(resp.currentPage)
            })
            .catch(error => console.log(error))
    }, []);

    return (
        <div className="productsPage">
            <p>Product: {title}</p>
            <p>Listing Type: {type}</p>
            <p>Price: {price}</p>
            <p>Total Revenue of Orders: {totalRevenue}</p>
            <br></br>
            <table>
                <thead>
                    <tr>
                        <td>Order ID</td>
                        <td>Full Name</td>
                        <td>Order Date</td>
                    </tr>
                </thead>
                <tbody>
                    {orders.map(order =>
                        <tr key={order.id}>
                            <td>{order.id}</td>
                            <td>{order.full_name}</td>
                            <td>{order.order_date}</td>
                        </tr>
                    )}
                </tbody>
                <br></br>
                <p>Imagine page navigation here</p>
            </table>
        </div>
    )
}

export default ProductPage;