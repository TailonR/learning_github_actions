import React from 'react';
import { NavLink } from './NavbarElements';
import { useLocation } from 'react-router-dom';


const Navbartabs = () => {
    const location = useLocation();

    return(
        <>
            {location.pathname === "/" ? (
                <NavLink to="/about">About</NavLink>
            ) : (
                <NavLink to="/">Home</NavLink>
            )}
        </>
    );
};

export default Navbartabs;