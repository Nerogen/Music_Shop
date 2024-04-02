import './App.css';
import axios from 'axios';
import React from 'react';


class App extends React.Component {
    state = { details: [], }

    componentDidMount() {
        console.log("I'm work");
        let data;
        axios.get('http://localhost:8000')
        .then(res => {
            data = res.data;
        this.setState({
            details: data
        });
        })
        .catch(err => {
            console.log(err);
        })
    }

    render() {
        return (
            <div>
              <header>Данные из django </header>
              <hr></hr>
              {this.state.details.map((output, id) => (
                <div key={id}>
                <div>
                <img src={output.image} alt="Product"/>
                <h2>{output.item_name}</h2>
                <h2>{output.cost}</h2>
                <h2>{output.info}</h2>
                </div></div>
              ))}
            </div>
        )
    }
}

export default App;
