import { useState, useEffect } from 'react'

export function RevenuePage() {
    const [revenue, setRevenue] = useState([] as any[])
    useEffect(() => {
        fetch("http://127.0.0.1:5001/api/total-revenue", {
            method: "GET",
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(resp => resp.json())
            .then(resp => setRevenue(resp.total))
            .catch(error => console.log(error))
    }, []);


    return (
        <div className="productsPage">
            <h1>Total Revenue: {revenue}</h1>
            <br></br>
            <p>Imagine a graph here</p>
        </div>

    );
}
export default RevenuePage;