import React from 'react';
import {List, Avatar, Card} from "antd";
import { SmileOutlined } from '@ant-design/icons';


const Products = props => {
    return (
        <List
            itemLayout="vertical"
            size="large"
            pagination={{
                onChange: page => {
                    console.log(page);
                },
                pageSize: 3
            }}
            dataSource={props.data}
            renderItem={item => (
                <List.Item
                    key={item.title}
                    actions={[
                        <SmileOutlined type="star-o" text="156" />,
                        <SmileOutlined type="like-o" text="156" />,
                        <SmileOutlined type="message" text="2" />
                    ]}

                extra={
                        <img
                            width={272}
                            alt="logo"
                            // src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
                            src = {item.image}
                        />
                    }
                >
                    <List.Item.Meta
                        avatar={<Avatar src={item.avatar} />}
                        title={<a href={`/${item.id}/`}> {item.title} </a>}
                        description={item.description}
                    />
                    {item.price}
                </List.Item>
            )}
        />
    );
};

export default Products;
