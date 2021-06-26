import Counter from "./Counter"

const Counters = () => {
    return (
        <div className="row">
            <div className="col-md-4">
                <Counter title="Total Submission" num="1530" />
            </div>
            <div className="col-md-4">
                <Counter title="Programming Problems" num="1530" />
            </div>
            <div className="col-md-4">
                <Counter title="Total User" num="1530" />
            </div>
        </div>
    )
}

export default Counters
