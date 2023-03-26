
function ApiServerInfo(props) {

    const apiAddress = props.api_base + '/server/info';

    function clickHandler() {
        fetch(apiAddress, {
            method: "GET",
            moe: "no-cors",
            header: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
            .then(response => response.json())
            .then(response => console.log(response))
    }
    return (
        <>
            <button onClick={clickHandler}>Request to Server:</button>
        </>
    );
}


export default ApiServerInfo;