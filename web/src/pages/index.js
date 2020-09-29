import React from "react"
import Layout from "../components/layout"
import Light from "../components/light"
import Thermostat from "../components/thermostat"

export default class IndexPage extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      error: null,
      isLoaded: false,
      inputValue: "",
      components: []
    }
    this.getComponents = this.getComponents.bind(this)
  }
  componentDidMount() {
    this.getComponents()
  }

  newLightInput(e) {
    e.preventDefault()
    // dont want re-rendering on each char input
    this.state.inputValue = e.target.value
  }

  addLight() {
    fetch(process.env.GATSBY_API_URL+"/components/light/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({"name": this.state.inputValue})
    })
      .then(res => res.json())
      .then(
        (result) => {
          if (parseInt(result.statusCode) >= 400)
            alert(`Server error: ${result.message}`)
          this.getComponents()
        },
        (error) => {
          alert(error)
        }
      )
  }

  getComponents() {
    fetch(process.env.GATSBY_API_URL+"/components")
      .then(res => res.json())
      .then(
        (result) => {
          console.log(result)
          this.setState({
            isLoaded: true,
            components: result.components
          })
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          })
          alert(error)
        }
      )
  }

  render() {
    return (
      <Layout>
        <div className="card" style={{marginTop: 10}}>
          <div className="card-header bg-light">
            <div className="row">
              <div className="col-lg-6">
                Home Components
              </div>
              <div className="col-lg-6">
                <div className="input-group mb-3" id="add-light">
                  <button className="btn btn-primary" style={{float: "right"}} onClick={this.addLight.bind(this)}>Add Light</button>
                  <input type="text" className="form-control" onChange={this.newLightInput.bind(this)}></input>
                </div>
              </div>
            </div>
          </div>
          <ul id="component-list" className="list-group list-group-flush">
              <li id="loading-indicator" className="list-group-item" hidden={this.state.isLoaded}>
                <div className="spinner-border text-primary" role="status" style={{float: "left"}}>
                  <span className="sr-only">Loading...</span>
                </div>
                <div className="text-primary" style={{float: "left", marginLeft: "5%"}}>Loading data ...</div>
              </li>
              {this.state.components.map((comp) => {
                if (comp.type === "Light")
                  return <Light props={comp} getComponents={this.getComponents}></Light>
                else if (comp.type === "Thermostat")
                  return<Thermostat props={comp}></Thermostat>
                return ""
              })}
            </ul>
        </div>
      </Layout>
    )
  }
}
