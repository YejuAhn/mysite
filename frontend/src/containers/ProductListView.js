import Products from "../components/Product";
import React from "react";
import CustomForm from "../components/Form";
import axios from "axios";


class ProductList extends React.Component {
    state = {
        products: []
    };

    fetchProducts = () => {
        axios.get("http://127.0.0.1:8000/api/products/").then(res => {
            this.setState({
                products: res.data
            });
            console.log(res.data)
        });
    }

    componentDidMount() {
        this.fetchProducts();
    }

    componentWillReceiveProps(newProps) {
        if (newProps.token) {
            this.fetchProducts();
        }
    }
    render() {
        return (
            <div>
                <Products data={this.state.products} /> <br />
                <h2> Create a Product </h2>
            </div>
        );
    }


    // state = {
    //     products: []
    // };
    //
    // fetchProducts = () => {
    //     axios.get("http://127.0.0.1:8000/api/products/").then(res => {
    //         this.setState({
    //             products: res.data
    //         });
    //     });
    // }
    //
    // componentDidMount() {
    //     this.fetchProducts();
    // }
    //
    // componentWillReceiveProps(newProps) {
    //     if (newProps.token) {
    //         this.fetchProducts();
    //     }
    // }
    //
    // render() {
    //     return (
    //         <div>
    //             <Product data={this.state.products} /> <br />
    //             <h2> Create an article </h2>
    //             <CustomForm requestType="post" articleID={null} btnText="Create" />
    //         </div>
    //     );
    // }
}

export default ProductList;

