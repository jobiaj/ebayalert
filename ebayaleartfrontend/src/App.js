import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";

const alertItems = [
  {
    id: 1,
    search_phrase: "Phone",
    interval: "2",
    email_address: "jobyalungal@gmail.com",
  },
  {
    id: 2,
    search_phrase: "Watch",
    interval: "30",
    email_address: "anjithathomas@gmail.com",
  },
  {
    id: 3,
    search_phrase: "Charger",
    interval: "5",
    email_address: "jithualungal@gmail.com",
  },
  {
    id: 4,
    search_phrase: "Phone",
    interval: "2",
    email_address: "athulds@gmail.com",
  },
];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      alertList: [],
      modal: false,
      activeItem: {
        search_phrase: "",
        interval: "",
        email_address: "",
      },
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/ebayalert/")
      .then((res) => this.setState({ alertList: res.data }))
      .catch((err) => console.log(err));
  };


  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();
    if (item.id) {
    axios
        .put(`/api/ebayalert/${item.id}/`, item)
        .then((res) => this.refreshList())
        .catch(function errorhandler(error) {
          alert(error);
        });
      return;
    }
    axios
      .post("/api/ebayalert/", item)
      .then((res) => this.refreshList())
      .catch(function errorhandler(error) {
        alert(error);
      });

  };

  handleDelete = (item) => {
    axios
      .delete(`/api/ebayalert/${item.id}/`)
      .then((res) => this.refreshList())
      .catch(function errorhandler(error) {
        alert(error);
      });
  };

  createItem = () => {
    const item = { search_phrase: "", interval: "", email_address: "" };

    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  renderTabList = () => {
    return (
      <div className="nav nav-tabs">
      </div>
    );
  };

  renderItems = () => {
    const newItems = this.state.alertList;

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`alert-title mr-2}`}
          title={item.description}
        >
          Search <b>{item.search_phrase}</b> in every <b> {item.interval} </b> minutes and send mail to <b> {item.email_address} </b>
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDelete(item)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Alert Scheduler</h1>
        <div className="row">
          <div className="col-md-12 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Create alert Scheduler
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}

export default App;