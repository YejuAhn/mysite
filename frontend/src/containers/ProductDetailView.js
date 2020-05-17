import Products from "../components/Product";
import React from "react";
import CustomForm from "../components/Form";
import axios from "axios";
import {Card} from 'antd';

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
        axios.interceptors.request.use(request => {
            console.log('Starting Request', request)
            return request
        })
    }
    render() {
        return (
            <Card title = {this.state.product.title}>
                <p> {this.state.product.description} </p>
            </Card>
        );
    }
}

export default ProductDetail;

