async function initMap() {
  // Request needed libraries.
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
  const map = new Map(document.getElementById("map"), {
    center: { lat: 37.736931001460505, lng: -1.3583551967829997 },
    zoom: 8,
    mapId: "4504f8b37365c3d0",
  });
  const marker = new AdvancedMarkerElement({
    map,
    position: { lat: 37.736931001460505, lng: -1.3583551967829997 },
  });
}

initMap();

