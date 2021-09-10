import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Schedule Info</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="alert-search_phrase">Search Pharse</Label>
              <Input
                type="text"
                id="alert-search_phrase"
                name="search_phrase"
                value={this.state.activeItem.search_phrase}
                onChange={this.handleChange}
                placeholder="Enter Search Pharse here"
              />
            </FormGroup>
            <FormGroup>
              <Label for="alert-interval">Search Interval</Label>
              <Input
                type="select"
                id="alert-interval"
                name="interval"
                value={this.state.activeItem.interval}
                onChange={this.handleChange}
                placeholder="Select your interval here"
              >
              <option value=''>Please select interval</option>
              <option value="2">2 minutes</option>
              <option value="10">10 minute</option>
              <option value="30">30 minutes</option>
              </Input>
            </FormGroup>
             <FormGroup>
              <Label for="alert-email_address">Email address of the user</Label>
              <Input
                type="text"
                id="alert-email_address"
                name="email_address"
                value={this.state.activeItem.email_address}
                onChange={this.handleChange}
                placeholder="Enter Search Pharse here"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}