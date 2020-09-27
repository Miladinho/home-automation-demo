import React from "react"

export default class Light extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            name: props.props.name,
            type:  props.props.type,
            status: props.props.status
        }
    }

    removeLight() {
        fetch(`${process.env.GATSBY_API_URL}/components/light/${this.state.name}`, {
            method: "DELETE",
        })
        .then(res => res.json())
        .then(
        (result) => {
            console.log(result)
            this.props.getComponents() // refresh
        },
        (error) => {
            console.log(error)
            alert(error)
        })
      }

    toggleLight(e) {
        e.preventDefault()
        const newStatus = this.state.status === 0? 1 : 0
        fetch(`${process.env.GATSBY_API_URL}/components/light/${this.state.name}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({"status": newStatus})
        })
        .then(res => res.json())
        .then(
        (result) => {
            console.log(result)
            this.setState({status: newStatus})
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
                        <strong>Status:</strong>
                    </div>
                    <div className="col-lg-3">
                        
                    </div>
                    <div className="col-lg-2"></div>
                </div>
                <div className="row">
                    <div className="col-lg-3">
                        {this.props.props.name}
                    </div>
                    <div className="col-lg-3">
                        <span className="badge badge-warning">{this.state.type}</span>
                    </div>
                    <div className="col-lg-1">
                        <span className="badge badge-primary badge-pill">{this.state.status === 1? "On": "Off"}</span>
                    </div>
                    <div className="col-lg-3">
                        <button type="button" className="btn btn-primary" onClick={this.toggleLight.bind(this)}>{this.state.status === 0? "Turn On": "Turn Off"}</button>
                    </div>
                    <div className="col-lg-2">
                    <button type="button" className="btn btn-danger" onClick={this.removeLight.bind(this)}>Remove</button>
                    </div>
                </div>
            </li>
        )
    }
}
