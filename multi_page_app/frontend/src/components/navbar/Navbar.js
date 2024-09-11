import React from 'react';
import { Nav, NavMenu } from './NavbarElements';
import Navbartabs from './NavbarTabs';

const Navbar = () => {
    return(
        <>
            <Nav>
                <NavMenu>
                    <Navbartabs />
                </NavMenu>
            </Nav>
        </>
    );
};

export default Navbar;