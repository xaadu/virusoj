import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import Footer from './components/Footer';

import Header from "./components/Header"
import About from './pages/About';
import NotFound_404 from './pages/Errors/NotFound_404';
import UnderDevelopment from './pages/Errors/UnderDevelopment';
import Home from './pages/Home';
import Problem from './pages/Problem';
import Problems from './pages/Problems';

const base_name = process.env.REACT_APP_BASENAME || '/'

function App() {

  return (
    <div className="App">
      <Router basename={base_name}>
        <Header />
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/problems' exact component={Problems} />
          <Route path='/problems/:id' component={Problem} /> 
          <Route path='/about' component={About} />

          <Route path='/login' component={UnderDevelopment} />
          <Route path='/register' component={UnderDevelopment} />

          <Route component={NotFound_404} />
        </Switch>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
