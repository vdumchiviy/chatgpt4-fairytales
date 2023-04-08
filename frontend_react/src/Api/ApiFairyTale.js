import React, { useState, useEffect } from 'react';


function ApiFairyTale(props) {

    const apiAddress = props.api_base + '/fairytale/new';
    const [fairyTale, setFairyTale] = useState('');
    const [fairytaleHero, setFairytaleHero] = useState('Misha');
    const [fairytaleTrend, setFairytaleTrend] = useState('mercy');
    const [fairytaleLanguage, setFairytaleLanguage] = useState('English');

    function handleInputHeroChange(event) {
        setFairytaleHero(event.target.value);
    }

    function handleInputTrendChange(event) {
        setFairytaleTrend(event.target.value);
    }

    function handleInputLanguageChange(event) {
        setFairytaleLanguage(event.target.value);
    }

    function clickHandler() {
        // document.getElementById('fairytale-hero').textContent = 'Misha';

        fetch(apiAddress + '?hero=' + fairytaleHero + '&language=' + fairytaleLanguage + '&trend=' + fairytaleTrend, {
            method: 'GET',
            // mode: "no-cors",
            header: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
            .then(response => response.json())
            .then(response => {
                console.log(response);
                setFairyTale(response.story);
            })
    }


    return (
        <>
            <div className='fairytale-container'>
                Enter the name(s) of hero:
                <input
                    className='fairytale-hero' id='fairytale-text' type="text"
                    value={fairytaleHero} onChange={handleInputHeroChange} /><br />
                Trend:
                <input
                    className='fairytale-trend' id='fairytale-trendt' type="text"
                    value={fairytaleTrend} onChange={handleInputTrendChange} /><br />
                Language:
                <select
                    className='fairytale-language' id='fairytale-language' type="text"
                    value={fairytaleLanguage} onChange={handleInputLanguageChange} >
                    <option value='English'>English</option>
                    <option value='Russian'>Russian</option>
                    <option value='Ukrainian'>Ukrainian</option>
                </select>

                <br />
                <button className='fairytale-button' onClick={clickHandler}>Get new faitytale</button><br />
                <textarea className='fairytale-text' id='fairytale-text' with="1200px" type="text" value={fairyTale} />
            </div>
        </>
    );
}

export default ApiFairyTale;