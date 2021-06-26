import { Link } from "react-router-dom"

const ProblemShortList = () => {
    return (
        <div className="problemShortList py-5">
            <div className="card">
                <div className="card-header">
                    Programming Problems to Solve
                </div>
                <div className="card-body text-start">
                    <table className="table table-striped table-hover">
                        <thead className="">
                            <tr>
                                <th scope="col">ID</th>
                                <th scope="col">Problem Title</th>
                                <th scope="col">Total Submission</th>
                                <th scope="col">Accepted Submission</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row">1001</th>
                                <td><Link to={`/problems/1001`} >First Awesome Problem</Link></td>
                                <td>600</td>
                                <td>159</td>
                            </tr>
                            <tr>
                                <th scope="row">1002</th>
                                <td><Link to={`/problems/1002`} >Second Awesome Problem</Link></td>
                                <td>325</td>
                                <td>124</td>
                            </tr>
                            <tr>
                                <th scope="row">1003</th>
                                <td><Link to={`/problems/1003`} >Third Awesome Problem</Link></td>
                                <td>256</td>
                                <td>97</td>
                            </tr>
                            <tr>
                                <th scope="row">1004</th>
                                <td><Link to={`/problems/1004`} >Fourth Awesome Problem</Link></td>
                                <td>128</td>
                                <td>69</td>
                            </tr>
                        </tbody>
                        <caption className="text-center">
                            <Link to='/problems' className="btn btn-outline-primary px-5 py-2 mt-4">All Problems</Link>
                        </caption>
                    </table>
                </div>
            </div>
        </div>
    )
}

export default ProblemShortList
