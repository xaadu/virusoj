import { Link } from "react-router-dom"

const UnderDevelopment = () => {
    return (
        <section id="err_not-found">
            <div className="container py-5">
                This Page is not yet completed! Please visit later. Thank You <br /> <br />

                <Link className="btn btn-outline-secondary" to='/'>Go Home</Link>

            </div>
        </section>
    )
}

export default UnderDevelopment
