// ======================================================
// GeoShield AI
// Utilities Module
// ======================================================

// ------------------------------------------------------
// Resource Colours
// ------------------------------------------------------

function getResourceColor(category) {

    switch (category) {

        case "Fire Station":
            return "red";

        case "Hospital":
            return "green";

        case "Police":
            return "blue";

        case "Military":
            return "black";

        case "Red Cross":
            return "crimson";

        case "Scouts":
            return "purple";

        case "St John":
            return "orange";

        case "NEMA":
            return "brown";

        default:
            return "#3388ff";

    }

}

// ------------------------------------------------------
// Resource Icons
// ------------------------------------------------------

function getResourceIcon(category) {

    switch (category) {

        case "Fire Station":
            return "🚒";

        case "Hospital":
            return "🏥";

        case "Police":
            return "👮";

        case "Military":
            return "🪖";

        case "Red Cross":
            return "⛑";

        case "Scouts":
            return "⚜️";

        case "St John":
            return "🚑";

        case "NEMA":
            return "🌍";

        default:
            return "📍";

    }

}

// ------------------------------------------------------
// Fire Risk
// ------------------------------------------------------

function getFireRisk(droughtRisk) {

    if (droughtRisk >= 70)
        return "HIGH";

    if (droughtRisk >= 40)
        return "MEDIUM";

    return "LOW";

}

// ------------------------------------------------------
// Flood Risk
// ------------------------------------------------------

function getFloodRisk(rainfall) {

    if (rainfall >= 1200)
        return "HIGH";

    if (rainfall >= 800)
        return "MEDIUM";

    return "LOW";

}

// ------------------------------------------------------
// ETA
// ------------------------------------------------------

function calculateETA(distanceKm) {

    return Math.ceil(distanceKm / 0.8);

}

// ------------------------------------------------------
// Number Formatting
// ------------------------------------------------------

function formatNumber(value, digits = 2) {

    return Number(value).toFixed(digits);

}

// ------------------------------------------------------
// Popup Builder
// ------------------------------------------------------

function buildResourcePopup(resource) {

    return `
<b>${getResourceIcon(resource.category)} ${resource.name}</b>

<hr>

<b>Category:</b> ${resource.category}<br>

<b>County:</b> ${resource.county}<br>

<b>Status:</b> ${resource.status}<br>

<b>Capacity:</b> ${resource.capacity}<br>

<b>Distance:</b> ${formatNumber(resource.distance_km)} km<br>

<b>ETA:</b> ${calculateETA(resource.distance_km)} mins<br>

<b>Contact:</b> ${resource.contact}
`;

}