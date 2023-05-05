import {
  BrowserRouter as Router,
  Route,
} from "react-router-dom";



import './App.css';
import Header from './components/Header'
import Pharmcy from './pages/pharmcy'
import PharmcyPagr from './pages/PharmcyPagr'
function App() {
  return (
    <Router>
    <div className="App">
      <Header/>
      <Route path="/" exact Component={Pharmcy}/>
      <Route path="/pharmcy/:id" Component={PharmcyPagr} />
    </div>
    </Router>
  );
}

export default App;
