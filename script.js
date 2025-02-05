function getWeather() {
    let city = document.getElementById("cityInput").value;
    let apiUrl = `http://127.0.0.1:5000/weather?city=${city}`;

    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("weatherResult").innerHTML = `<p style="color:red;">${data.error}</p>`;
        } else {
            let iconUrl = `http://openweathermap.org/img/wn/${data.icon}@2x.png`;
            document.getElementById("weatherResult").innerHTML = `
                <h2>${data.city}</h2>
                <img src="${iconUrl}" alt="Weather Icon">
                <p><strong>🌡 Nhiệt độ:</strong> ${data.temperature}°C</p>
                <p><strong>💧 Độ ẩm:</strong> ${data.humidity}%</p>
                <p><strong>🌬️ Tốc độ gió:</strong> ${data.wind_speed} m/s</p>
                <p><strong>📖 Mô tả:</strong> ${data.description}</p>
            `;
        }
    })
    .catch(error => {
        document.getElementById("weatherResult").innerHTML = `<p style="color:red;">Lỗi kết nối đến API!</p>`;
    });
}
