import React, { useState, useEffect } from 'react';



function ApiServerInfo(props) {

    const apiAddress = props.api_base + '/server/info';
    const [serverInfo, setServerInfo] = useState('');

    function clickHandler() {
        fetch(apiAddress, {
            method: "GET",
            // mode: "no-cors",
            header: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
            .then(response => response.json())
            .then(response => {
                console.log(response.version);
                setServerInfo(response.version);
            })
    }
    return (
        <>
            <button onClick={clickHandler}>Request to Server:</button>
            <div>version: {serverInfo} </div>
        </>
    );
}


export default ApiServerInfo;