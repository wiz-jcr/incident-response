function drawChart(array1, array2) {
    LOC = document.getElementById('chart');

    var label = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

    var respData = getAPIData();

    var trace1 = {
        x: label,
        y: respData.incidence,
        name: 'New Incidents',
        type: 'bar',
        marker: {
            color: '#0095FF'
        }
    };
    
    var trace2 = {
        x: label,
        y: respData.resolved,
        name: 'Closed Incidents',
        type: 'bar',
        marker: {
            color: '#00E096'
        }
    };
    
    var data = [trace1, trace2];
    
    var layout = {barmode: 'group'};
    
    Plotly.newPlot(LOC, data, layout);
};

function getAPIData(){
    var responseData = {
        'incidence': Array.from({length: 12}, () => Math.floor(Math.random() * 100)),
        'resolved': Array.from({length: 12}, () => Math.floor(Math.random() * 100)),
    };

    return responseData
}