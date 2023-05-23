import { NavLink } from "react-router-dom";

import "./styles.css";

export function NavBar() {
    return (
        <nav className="navbar-container">
            <NavLink to="/products">Products</NavLink>
            <NavLink to="/revenue">Revenue</NavLink>
        </nav>
    );
}

export default NavBar;