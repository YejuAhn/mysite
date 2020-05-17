import Products from "../components/Product";
import React from "react";
import CustomForm from "../components/Form";
import axios from "axios";
import {Card} from 'antd';
import {Link} from 'react-router-dom';

class ProductDetail extends React.Component {
    state = {
        product: {}
    };

    componentDidMount() {
        const id = this.props.match.params.id;
        axios.get(`http://127.0.0.1:8000/api/products/${id}/`).then(res => {
            this.setState({
                product: res.data
            });
        });
    }
    render() {
        return (
            <Card title = {this.state.product.title}>
                <p> {this.state.product.description} </p>
                <p> {this.state.product.summary} </p>
                <p> {this.state.product.price} </p>
                <img width={272} src={this.state.product.image}  alt="image"/>
                <p> {this.state.product.url}</p>
            </Card>
        );
    }
}

export default ProductDetail;

