import React from "react";

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './NavBar';

import ProductPage from "./pages/ProductPage";
import ProductsPage from "./pages/ProductsPage";
import RevenuePage from "./pages/RevenuePage";

let App = () => {
    return (
        <BrowserRouter>
            <Navbar />
            <Routes>
                <Route path="/" element={<ProductsPage />} />
                <Route path="/products" element={<ProductsPage />} />
                <Route path="/product" element={<ProductPage />} />
                <Route path="/revenue" element={<RevenuePage />} />
            </Routes>
        </BrowserRouter>
    );
};
export default App;
