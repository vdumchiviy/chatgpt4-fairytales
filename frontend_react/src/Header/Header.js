function Header(props) {
    return (
        <header>
            <h1 className="header-h1">ChatGPT Short Fairy Tale</h1>
            <Nav nav={props.data.nav}></Nav>
        </header>
    );
}

function Nav(props) {
    let nav = props.nav;
    const listItem = nav.map(item => <li key={item.link}><a href={item.link}>{item.text}</a></li>);
    return (
        <nav>
            {listItem}
        </nav>
    );
}


export default Header;