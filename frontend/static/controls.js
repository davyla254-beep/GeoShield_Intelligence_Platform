// ======================================================
// Controls Module
// ======================================================

function initializeControls() {

    // ----------------------------
    // Search
    // ----------------------------

    L.Control.geocoder({
        defaultMarkGeocode: false
    })

    .on("markgeocode", function (e) {

        const center = e.geocode.center;

        map.setView(center, 12);

    })

    .addTo(map);

    // ----------------------------
    // Locate Button
    // ----------------------------

    const locateBtn = document.getElementById("locateBtn");

    if (locateBtn) {

        locateBtn.addEventListener("click", function () {

            map.locate({

                setView: true,
                maxZoom: 13

            });

        });

    }

    // ----------------------------
    // Location Found
    // ----------------------------

    map.on("locationfound", function (e) {

        window.currentIncident = {

            lat: e.latitude,
            lng: e.longitude

        };

        L.marker([e.latitude, e.longitude])

            .addTo(map)

            .bindPopup("📍 Current Incident Location")

            .openPopup();

    });

    // ----------------------------
    // Location Error
    // ----------------------------

    map.on("locationerror", function () {

        alert("Unable to access your location.");

    });

}