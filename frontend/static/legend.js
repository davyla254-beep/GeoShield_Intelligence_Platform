// ======================================================
// Legend Module
// ======================================================

function createLegend(){

    const legend = L.control({

        position:"bottomleft"

    });

    legend.onAdd=function(){

        const div=L.DomUtil.create("div","legend");

        div.innerHTML=`

<b>🔥 Fire Intensity</b><br><br>

<span style="display:inline-block;width:15px;height:15px;background:#FFD400;border-radius:50%;"></span>
Low<br>

<span style="display:inline-block;width:15px;height:15px;background:#FF8C00;border-radius:50%;"></span>
Moderate<br>

<span style="display:inline-block;width:15px;height:15px;background:#FF3B30;border-radius:50%;"></span>
High<br>

<span style="display:inline-block;width:15px;height:15px;background:#8A2BE2;border-radius:50%;"></span>
Extreme

`;

        return div;

    };

    legend.addTo(map);

}