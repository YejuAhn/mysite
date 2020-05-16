import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'antd/dist/antd.css';
import CustomLayout from "./containers/Layout";
import ProductList from "./containers/ProductListView";
function App() {
  return (
    <div className="App">
      <CustomLayout>
          <ProductList/>
      </CustomLayout>
    </div>
  );
}

export default App;
