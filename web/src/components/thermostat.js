import React from "react"

export default class Thermostat extends React.Component {
    constructor(props) {
      super(props)
      this.state = {
        inputValue: 0,
        name: props.props.name,
        type: props.props.type,
        temperature: props.props.temperature
      }
    }

    temperatureInput(e) {
        e.preventDefault()
        // dont want re-rendering on each char input
        this.state.inputValue = e.target.value
    }

    setThermostat(e) {
        e.preventDefault()
        fetch(process.env.GATSBY_API_URL+"/components/thermostat", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({"value": this.state.inputValue})
        })
        .then(res => res.json())
        .then(
        (result) => {
            console.log(result)
            this.setState({temperature: this.state.inputValue})
        },
        (error) => {
            console.log(error)
            alert(error)
        })
    }

    render() {
        return (
            <li className="list-group-item">
                <div className="row">
                    <div className="col-lg-3">
                        <strong>Name:</strong>
                    </div>
                    <div className="col-lg-3">
                        <strong>Type:</strong>
                    </div>
                    <div className="col-lg-1">
                        <strong>Temp:</strong>
                    </div>
                    <div className="col-lg-3">
                        
                    </div>
                    <div className="col-lg-2"></div>
                </div>
                <div className="row">
                    <div className="col-lg-3">
                        {this.state.name}
                    </div>
                    <div className="col-lg-3">
                        <span className="badge badge-danger">{this.state.type}</span>
                    </div>
                    <div className="col-lg-1">
                        <span id="temp-value" className="badge badge-primary badge-pill">{this.state.temperature}</span>
                    </div>
                    <div className="col-lg-3">
                        <div className="input-group mb-3">
                            <div className="input-group-prepend">
                                <button type="button" className="btn btn-primary input-group-buttopn" onClick={this.setThermostat.bind(this)}>Set</button>
                            </div>
                            <input type="text" className="form-control" onChange={this.temperatureInput.bind(this)}></input>
                        </div>
                    </div>
                </div>
            </li>
        )
    }
}
