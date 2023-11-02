const dataContainer = document.getByElementById('data-container');
const botStatus = document.getByElementById('bot-status');
const gainsDisplay = document.getByElementById('gains');
const lossesDisplay = document. getByElementById('losses');

let gainsAmount = 0;
let lossesAmount = 0;

function updateTradingData(tradingData) {
    const dataHTML = tradingData.map((data) => {
        return `<div><strong>Time:</strong> ${data.time}, <strong>Price:</strong> ${data.price}, <strong>Action:</strong> ${data.action}</div>`;
    });
    dataContainer.innerHTML = dataHTML.join('');
}

//updates the gains and losses
function updateGainsAndLosses(action, price){
    if(action === 'Buy'){
        gainsAmount += price;
    } else if(action === 'Sell'){
        lossesAmount += price;
    }

    gainsDisplay.textContent = gainsAmount.toFixed(2);
    lossesDisplay.textContent = lossesAmount.toFixed(2)
}

function fetchTradingData(){

    fetch('https://developer.oanda.com/rest-live-v20/instrument-ep/#collapse_endpoint_2')
        .then(response => response.json())
        .then(data => {
            updateTradingData(data);
        })
        .catch(error => {
            console.log('Error fetching trading data: ', error);
        });
}

function updateDataAndSimulateActions() {
    fetchTradingData();
    // Simulate bot actions based on the fetched data or call your bot's API here
}

// Update data and simulate actions every 3 seconds (replace with real-time updates)
setInterval(updateDataAndSimulateActions, 3000);

// Initial update
updateDataAndSimulateActions();