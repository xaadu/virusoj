import { Link } from "react-router-dom"

const NotFound_404 = () => {
    return (
        <section id="err_not-found">
            <div className="container py-5">
                Page Not Found! <br /> <br />

                <Link className="btn btn-outline-secondary" to='/'>Go Home</Link>

            </div>
        </section>
    )
}

export default NotFound_404
