(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{110:function(e,t,a){e.exports=a(208)},115:function(e,t,a){},116:function(e,t,a){},187:function(e,t){},208:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),c=a(5),o=a.n(c),l=(a(115),a(116),a(117),a(210)),i=a(69),u=a(216),s=a(35),m=l.a.Header,d=l.a.Content,p=l.a.Footer,h=function(e){return r.a.createElement(l.a,{className:"layout"},r.a.createElement(m,null,r.a.createElement("div",{className:"logo"}),r.a.createElement(i.a,{theme:"dark",mode:"horizontal",defaultSelectedKeys:["2"]},r.a.createElement(i.a.Item,{key:"1"},"nav 1"),r.a.createElement(i.a.Item,{key:"2"},"nav 2"),r.a.createElement(i.a.Item,{key:"3"},"nav 3"))),r.a.createElement(d,{style:{padding:"0 50px"}},r.a.createElement(u.a,{style:{margin:"16px 0"}},r.a.createElement(u.a.Item,null,r.a.createElement(s.b,{to:"/"}," Home ")),r.a.createElement(u.a.Item,null,r.a.createElement(s.b,{to:"/"}," List "))),r.a.createElement("div",{className:"site-layout-content"},e.children)),r.a.createElement(p,{style:{textAlign:"center"}},"Ant Design \xa92018 Created by Ant UED"))},E=a(6),f=a(46),v=a(47),g=a(54),y=a(55),b=a(214),k=a(213),w=a(217),x=function(e){return r.a.createElement(b.b,{itemLayout:"vertical",size:"large",pagination:{onChange:function(e){console.log(e)},pageSize:3},dataSource:e.data,renderItem:function(e){return r.a.createElement(b.b.Item,{key:e.title,actions:[r.a.createElement(w.a,{type:"star-o",text:"156"}),r.a.createElement(w.a,{type:"like-o",text:"156"}),r.a.createElement(w.a,{type:"message",text:"2"})],extra:r.a.createElement("img",{width:272,alt:"logo",src:e.image})},r.a.createElement(b.b.Item.Meta,{avatar:r.a.createElement(k.a,{src:e.avatar}),title:r.a.createElement("a",{href:"/".concat(e.id,"/")}," ",e.title," "),description:e.description}),e.price)}})},I=(a(187),a(52)),j=a.n(I),O=function(e){Object(g.a)(a,e);var t=Object(y.a)(a);function a(){var e;Object(f.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={products:[]},e.fetchProducts=function(){j.a.get("http://127.0.0.1:8000/api/products/").then((function(t){e.setState({products:t.data}),console.log(t.data)}))},e}return Object(v.a)(a,[{key:"componentDidMount",value:function(){this.fetchProducts()}},{key:"componentWillReceiveProps",value:function(e){e.token&&this.fetchProducts()}},{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement(x,{data:this.state.products})," ",r.a.createElement("br",null),r.a.createElement("h2",null," Create a Product "))}}]),a}(r.a.Component),A=a(215),C=function(e){Object(g.a)(a,e);var t=Object(y.a)(a);function a(){var e;Object(f.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={product:{}},e}return Object(v.a)(a,[{key:"componentDidMount",value:function(){var e=this,t=this.props.match.params.id;j.a.get("http://127.0.0.1:8000/api/products/".concat(t,"/")).then((function(t){e.setState({product:t.data})}))}},{key:"render",value:function(){return r.a.createElement(A.a,{title:this.state.product.title},r.a.createElement("p",null," ",this.state.product.description," "),r.a.createElement("p",null," ",this.state.product.summary," "),r.a.createElement("p",null," ",this.state.product.price," "),r.a.createElement("img",{width:272,src:this.state.product.image,alt:"image"}),r.a.createElement("p",null," ",this.state.product.url))}}]),a}(r.a.Component),P=function(){return r.a.createElement("div",null,r.a.createElement(E.a,{exact:!0,path:"/",component:O})," ",r.a.createElement(E.a,{exact:!0,path:"/:id",component:C})," ")};var S=function(){return r.a.createElement("div",{className:"App"},r.a.createElement(s.a,null,r.a.createElement(h,null,r.a.createElement(P,null))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(r.a.createElement(S,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[110,1,2]]]);
//# sourceMappingURL=main.9c7b1e98.chunk.js.map