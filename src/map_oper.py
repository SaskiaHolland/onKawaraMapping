import logging

import folium
from folium.plugins import MarkerCluster

from src import geo_handler, utils
from src.utils import CSV_FILE, MISSING_FILE

# from IPython.display import IFrame

logger = logging.getLogger(__name__)


def _save_missing_city(city: str) -> None:
    with open(MISSING_FILE, "a", encoding="utf-8") as f:
        f.write(city + ", ")
    logger.warning(f"Missing coordinates for city: {city}")
    print(f"Missing coordinates for city: {city}")


def _create_popup_html(row) -> str:
    title = row[2].replace('"', "")
    creator = row[5]
    date = row[9]
    classification = row[12]
    serie = row[13]
    material = row[7]
    measure = row[6]

    second_title = row[3] if isinstance(row[3], str) else ""
    link = row[15] if isinstance(row[15], str) else ""
    creditline = row[16] if isinstance(row[16], str) else ""

    image_html = (
        f'<img src="{link}" width="316" height="252" alt="{creditline}">'
        if link
        else ""
    )

    html = f"""
    <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                table {{ width: 100%; font-size: small; }}
                th {{ text-align: left; color: #72797F; font-size: x-small; }}
            </style>
        </head>
        <body>
            <h2>{title}</h2>
            {image_html}
            <h3>{second_title}</h3>
            <table>
                <tr><th>Creator</th><td>{creator}</td></tr>
                <tr><th>Creation date</th><td>{date}</td></tr>
                <tr><th>Materials</th><td>{material}</td></tr>
                <tr><th>Measurements</th><td>{measure}</td></tr>
                <tr><th>Classification</th><td>{classification}</td></tr>
                <tr><th>Related Work</th><td>{serie}</td></tr>
            </table>
        </body>
    </html>
    """
    return html


def creating_map() -> folium.Map:
    table = utils.open_csv(CSV_FILE)
    coordinates = geo_handler.get_location()

    m = folium.Map(tiles="cartodb positron", location=[47.3941, 0.6848], zoom_start=5)

    marker_cluster_city = MarkerCluster(name="city").add_to(m)

    for row in table.itertuples():
        city = row[10]
        coords = coordinates.get(city, [])

        if not coords:
            _save_missing_city(city)
            continue

        html = _create_popup_html(row)

        iframe = folium.IFrame(html)
        popup = folium.Popup(
            iframe,
            min_width=400,
            max_width=450,
            min_height=350,
            max_height=400,
            sticky=True,
        )

        folium.Marker(
            location=coords,
            popup=popup,
            tooltip=f"{city}",
            icon=folium.Icon(color="red", prefix="fa", icon="camera-retro"),
        ).add_to(marker_cluster_city)

    return m
