// ======================================================
// Fire Module
// ======================================================

function loadFireHotspots() {

    fetch("/alerts")

        .then(response => response.json())

        .then(data => {

            fireLayer.clearLayers();

            if (!data.alerts)
                return;

            data.alerts.forEach(alert => {

                let radius = 6;
                let fill = "#FFD400";
                let border = "#FF8C00";

                if (alert.frp >= 10) {

                    radius = 9;
                    fill = "#FF8C00";
                    border = "#CC5500";

                }

                if (alert.frp >= 25) {

                    radius = 12;
                    fill = "#FF3B30";
                    border = "#8B0000";

                }

                if (alert.frp >= 60) {

                    radius = 16;
                    fill = "#8A2BE2";
                    border = "#4B0082";

                }

                L.circleMarker(

                    [alert.latitude, alert.longitude],

                    {

                        radius,

                        color: border,

                        fillColor: fill,

                        fillOpacity: 0.9,

                        weight: 2

                    }

                )

                .bindPopup(

`<b>🔥 Wildfire</b><br>
FRP: ${alert.frp}<br>
Brightness: ${alert.brightness}<br>
Detected: ${alert.time}`

                )

                .addTo(fireLayer);

            });

        })

        .catch(console.error);

}