import { NavLink } from "react-router-dom"

const Header = () => {
    return (
        <header className="header">
            <nav className="navbar navbar-expand-md navbar-light bg-light">
                <div className="container">
                    <NavLink className="navbar-brand" to='/'>Virus OJ</NavLink>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNavDropdown">
                        <ul className="navbar-nav">
                            <li className="nav-item px-md-4">
                                <NavLink
                                    className="nav-link"
                                    activeClassName="active"
                                    to='/' exact
                                >Home</NavLink>
                            </li>
                            <li className="nav-item px-md-4">
                                <NavLink
                                    className="nav-link"
                                    activeClassName="active"
                                    to='/problems'
                                >Problems</NavLink>
                            </li>
                            <li className="nav-item ps-md-4">
                                <NavLink
                                    className="nav-link"
                                    activeClassName="active"
                                    to='/about'
                                >About</NavLink>
                            </li>
                        </ul>
                        <ul className="navbar-nav ms-auto">
                            <li className="nav-item px-md-4">
                                <NavLink
                                    className="nav-link"
                                    activeClassName="active"
                                    to='/login' exact
                                >Login</NavLink>
                            </li>
                            <li className="nav-item px-md-4">
                                <NavLink
                                    className="nav-link"
                                    activeClassName="active"
                                    to='/register'
                                >Register</NavLink>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </header>
    )
}

export default Header
