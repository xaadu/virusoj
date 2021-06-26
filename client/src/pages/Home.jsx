import Counters from "../components/Counters/Counters"
import ProblemShortList from "../components/problemShortList/ProblemShortList"

const Home = () => {
    return (
        <section id="home">
            <div className="container text-center py-5">
                <div className="welcome py-5">
                    <h2 className="display-1">Welcome to Virus OJ</h2>
                    <h2 className="h4">The ultimate Practice Ground for beginners.</h2>
                </div>

                <div className="counters py-5">
                    <h2 className="display-6">Site Statistics</h2>
                    <Counters />
                </div>

                <ProblemShortList />

            </div>
        </section>
    )
}

export default Home
