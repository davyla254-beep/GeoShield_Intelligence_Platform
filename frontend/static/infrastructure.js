// ======================================================
// GeoShield AI
// Infrastructure Module
// ======================================================

// ------------------------------------
// Draw Response Route
// ------------------------------------

function drawResponseRoute(resource) {

    responseLayer.clearLayers();

    if (!window.currentIncident)
        return;

    L.polyline(

        [

            [resource.latitude, resource.longitude],

            [window.currentIncident.lat, window.currentIncident.lng]

        ],

        {

            color: "#00ffff",

            weight: 3,

            dashArray: "10 8"

        }

    ).addTo(responseLayer);

}

// ------------------------------------
// Load Infrastructure
// ------------------------------------

function loadInfrastructure(county) {

    infrastructureLayer.clearLayers();

    fetch("/resources/" + encodeURIComponent(county))

        .then(response => response.json())

        .then(resources => {

            const incident =
                document.getElementById("incidentType").value;

            let allowed = [];

            switch (incident) {

                case "Fire":

                    allowed = [

                        "Fire Station",

                        "Hospital",

                        "Police",

                        "Military",

                        "Red Cross",

                        "St John"

                    ];

                    break;

                case "Flood":

                    allowed = [

                        "Hospital",

                        "Military",

                        "Police",

                        "Red Cross",

                        "Scouts",

                        "St John",

                        "NEMA"

                    ];

                    break;

                case "Earthquake":

                    allowed = [

                        "Hospital",

                        "Military",

                        "Police",

                        "Fire Station",

                        "Red Cross",

                        "Scouts",

                        "St John",

                        "NEMA"

                    ];

                    break;

                case "Disease":

                    allowed = [

                        "Hospital",

                        "Red Cross",

                        "St John",

                        "NEMA"

                    ];

                    break;

                case "Drought":

                    allowed = [

                        "Military",

                        "Police",

                        "Red Cross",

                        "Scouts",

                        "NEMA"

                    ];

                    break;

            }

            resources

                .filter(resource =>

                    allowed.includes(resource.category)

                )

                .forEach(resource => {

                    const color = getResourceColor(resource.category);

const emoji = getResourceIcon(resource.category);

                    const marker = L.circleMarker(

                        [

                            resource.latitude,

                            resource.longitude

                        ],

                        {

                            radius: 8,

                            color: color,

                            fillColor: color,

                            fillOpacity: 1,

                            weight: 2

                        }

                    );

                   marker.bindPopup(buildResourcePopup(resource));

                    marker.addTo(infrastructureLayer);

                    marker.on("click", function () {

                        drawResponseRoute(resource);

                    });

                });

        })

        .catch(console.error);

}

// ======================================================
// Incident Selector
// ======================================================

const incidentSelector = document.getElementById("incidentType");

if (incidentSelector) {

    incidentSelector.addEventListener("change", function () {

        if (!window.currentCounty)
            return;

        loadInfrastructure(window.currentCounty);

    });

}