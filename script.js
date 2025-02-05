function getWeather() {
    let city = document.getElementById("cityInput").value;
    let apiKey = "392b44d861bff9b6fac2585893b51903"; // Thay bằng API Key mới

    fetch(`http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`)
    .then(response => response.json())
    .then(data => {
        if (data.cod === 200) {
            document.getElementById("weatherResult").innerHTML = `
                <p><strong>Thành phố:</strong> ${data.name}</p>
                <p><strong>Nhiệt độ:</strong> ${data.main.temp}°C</p>
                <p><strong>Độ ẩm:</strong> ${data.main.humidity}%</p>
                <p><strong>Mô tả:</strong> ${data.weather[0].description}</p>
            `;
        } else {
            document.getElementById("weatherResult").innerHTML = `<p style="color:red;">Không thể lấy dữ liệu thời tiết!</p>`;
        }
    })
    .catch(error => {
        document.getElementById("weatherResult").innerHTML = `<p style="color:red;">Lỗi kết nối đến API!</p>`;
        console.error(error);
    });
}
