from util import *
from folium.plugins import MarkerCluster
import folium
#from IPython.display import IFrame

def creatingMap():
    # plotting all citys as groups
    m = folium.Map(tiles="cartodb positron", location=[47.3941, 0.6848], zoom_start=5)

    #create a marker cluster
    marker_cluster_city = folium.plugins.MarkerCluster(name='city').add_to(m)

    table = openCSV('./data/on_kawara_data.csv')

    coordinates = getLocation()

    for row in table.itertuples():
        title = row[2].replace('"','')
        creator = row[5]
        date = row[9]
        classification = row[12]
        serie = row[13]
        material = row[7]
        measure = row[6]
        city = row[10]
        
        # link & second_title
        if type(row[3]) == str and type(row[15]) == str:
            second_title = row[3]
            link = row[15]
            creditline = row[16]
            icon = folium.Icon(color='red', prefix='fa', icon='camera-retro')
            html = f'''
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <style>
                                body {{ font-family:arial, 'lucida console', sans-serif;  }}
                            </style>
                        </head>
                        <body>
                            <h2 style="font-family:arial, 'lucida console', sans-serif;">{title}</h2>
                            <img src={link} width="316" height="252" alt={creditline}>
                            <h3 style="font-family:arial, 'lucida console', sans-serif;">{second_title}</h3>
                            <table style="height: 126px; width: 370px; font-family:arial, 'lucida console', sans-serif;">
                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Creator</th>
                                        <th>Creation date</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{creator}</td>
                                        <td>{date}</td>
                                    </tr>
                                </tbody>

                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Materials and Techniques</th>
                                        <th>Measurements</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{material}</td>
                                        <td>{measure}</td>
                                    </tr>
                                </tbody>

                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Classification</th>
                                        <th>Related Work</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{classification}</td>
                                        <td>{serie}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </body>
                    </html>
                '''
            iframe = folium.IFrame(html)
            popup = folium.Popup(iframe, min_width=400, max_width=500, min_height=400, max_height=500, sticky=True)
            
        # second_title but no link
        elif type(row[3]) == str and type(row[15]) != str:
            second_title = row[3]
            icon = folium.Icon(color='red')
            html = f'''
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <style>
                                body {{ font-family:arial, 'lucida console', sans-serif;  }}
                            </style>
                        </head>
                        <body>
                        <h2 >{title}</h2>
                            <h3 >{second_title}</h3>
                            <table style="height: 126px; width: 370px; font-family:arial, 'lucida console', sans-serif;">
                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Creator</th>
                                        <th>Creation date</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{creator}</td>
                                        <td>{date}</td>
                                    </tr>
                                </tbody>

                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Materials and Techniques</th>
                                        <th>Measurements</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{material}</td>
                                        <td>{measure}</td>
                                    </tr>
                                </tbody>

                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Classification</th>
                                        <th>Related Work</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{classification}</td>
                                        <td>{serie}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </body>
                    </html>
            '''
            iframe = folium.IFrame(html)
            popup = folium.Popup(iframe, min_width=400, max_width=450, min_height=350, max_height=450, sticky=True)

        #link but no second_title    
        elif type(row[3]) != str and type(row[15]) == str:
            link = row[15]
            icon = folium.Icon(color='red', prefix='fa', icon='camera-retro')
            html = f'''
                    <!DOCTYPE html>
                    <html>
                         <head>
                            <style>
                                body {{ font-family:arial, 'lucida console', sans-serif;  }}
                            </style>
                        </head>
                        <body>
                            <h2 style="font-family:arial, 'lucida console', sans-serif;">{title}</h2>
                            <img src={link} width="316" height="252" alt={title}>
                            <table style="height: 126px; width: 370px; font-family:arial, 'lucida console', sans-serif;">
                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Creator</th>
                                        <th>Creation date</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{creator}</td>
                                        <td>{date}</td>
                                    </tr>
                                </tbody>

                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Materials and Techniques</th>
                                        <th>Measurements</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{material}</td>
                                        <td>{measure}</td>
                                    </tr>
                                </tbody>

                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Classification</th>
                                        <th>Related Work</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{classification}</td>
                                        <td>{serie}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </body>
                    </html>
                '''
            iframe = folium.IFrame(html)
            popup = folium.Popup(iframe, min_width=400, max_width=500, min_height=350, max_height=400, sticky=True)
        
        # standard case
        else:
            icon = folium.Icon(color='red')
            html = f'''
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <style>
                                body {{ font-family:arial, 'lucida console', sans-serif;  }}
                            </style>
                        </head>
                        <body>
                            <h2>{title}</h2>
                            <table style="height: 126px; width: 370px;">
                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Creator</th>
                                        <th>Creation date</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{creator}</td>
                                        <td>{date}</td>
                                    </tr>
                                </tbody>

                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Materials and Techniques</th>
                                        <th>Measurements</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{material}</td>
                                        <td>{measure}</td>
                                    </tr>
                                </tbody>

                                <thead>
                                    <tr style="text-align: left; color: #72797F; font-size: x-small;">
                                        <th>Classification</th>
                                        <th>Related Work</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>{classification}</td>
                                        <td>{serie}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </body>
                    </html>
                '''
            iframe = folium.IFrame(html)
            popup = folium.Popup(iframe, min_width=400, max_width=450, min_height=350, max_height=400, sticky=True)
        
        if coordinates[city] != []:       
            folium.Marker(
                coordinates[city], 
                popup=popup, 
                tooltip=f'{city}', 
                icon=icon,
            ).add_to(marker_cluster_city)
        else:
            with open('output/cities_without_coordinates.txt', 'w') as f:
                f.write(city + ', ')
                f.close


    return m 