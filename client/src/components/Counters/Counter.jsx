const Counter = ({ title, num }) => {
    return (
        <div className="card">
            <div className="card-header">
                {title}
            </div>
            <div className="card-body">
                <h1 className="card-title display-1">{num}</h1>
            </div>
        </div>
    )
}

export default Counter
