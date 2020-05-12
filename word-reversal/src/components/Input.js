import React from 'react';

class Input extends React.Component {

    constructor(props) {
        super(props);
        this.state = {text: '', result: 'Result'};
      }

    onClick(event) {
        this.setState({result:this.state.text.split("").reverse().join("")})
      }
  

    render() {
        return (
        <div className="container addtask">
            <div className="row">
                <div className="col-5 offset-4">
                    <h1>Enter text to be reversed here: </h1>
                </div>
            </div>
            <div className="row">
                <div className="col-5 offset-4">
                    <div className="input-group mb-3">
                        <input
                            type="text"
                            className="form-control"
                            placeholder="Enter text..."
                            onChange={this.taskDescriptionChanged}
                        />
                        <div className="input-group-append">
                            <button className="btn addButton btn-outline-primary" type="button" onClick={this.onClick.bind(this)}>
                                Submit
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        )
    };
}



export default Input;