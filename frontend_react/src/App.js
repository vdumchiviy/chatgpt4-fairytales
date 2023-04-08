import Header from "./Header/Header";
import ApiServerInfo from "./Api/ApiServerInfo";
import ApiFairyTale from "./Api/ApiFairyTale";

const headerData = {
  nav: [
    { "key": 1, "text": "Home", "link": "index.html" },
    { "key": 2, "text": "Contacts", "link": "contacts.html" },
    { "key": 3, "text": "About", "link": "About.html" },
  ]
}

const debug = true;
let apiAddress;

if (debug) {
  apiAddress = "http://127.0.0.1:8000"
}
function App() {
  return (
    <>
      <Header data={headerData}></Header>
      <img className="main-image" src="/images/lisaikolobok.jpg" alt="main-image" title="Lisa i Kolobok" />
      <p className="text">Settings:</p>

      <ApiServerInfo api_base={apiAddress}></ApiServerInfo>
      <ApiFairyTale api_base={apiAddress}></ApiFairyTale>


    </>

  );
}

export default App;
