async function fetchData() {
    try {
        // Status
        const statusRes = await fetch('http://127.0.0.1:8000/api/status');
        const statusData = await statusRes.json();
        document.getElementById('status').innerText = `System: ${statusData.status}`;

        // Account
        const accRes = await fetch('http://127.0.0.1:8000/api/account');
        const accData = await accRes.json();
        document.getElementById('account').innerHTML = `
            <p>Status: ${accData.status}</p>
            <p>Cash: $${parseFloat(accData.cash).toFixed(2)}</p>
            <p>Buying Power: $${parseFloat(accData.buying_power).toFixed(2)}</p>
        `;

        // Market
        const marketRes = await fetch('http://127.0.0.1:8000/api/market');
        const marketData = await marketRes.json();
        document.getElementById('market').innerHTML = `
            <p>Regime: <strong>${marketData.regime}</strong></p>
            <p>Confidence: ${marketData.confidence}</p>
        `;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

fetchData();
setInterval(fetchData, 60000); // refresh every minute
