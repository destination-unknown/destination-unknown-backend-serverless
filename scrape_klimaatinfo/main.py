from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

properties_all_countries = pd.DataFrame()
countries = ['Afghanistan'
,'Albanie'
,'Algerije'
,'Amerikaans-Samoa'
,'Amerikaanse-Maagdeneilanden'
,'Andorra'
,'Angola'
,'Anguilla'
,'Antarctica'
,'Antigua-en-Barbuda'
,'Argentinie'
,'Armenie'
,'Aruba'
,'Australie'
,'Azerbeidzjan'
,'Bahamas'
,'Bahrein'
,'Bangladesh'
,'Barbados'
,'Belgie'
,'Belize'
,'Benin'
,'Bermuda'
,'Bhutan'
,'Bolivia'
,'Bonaire'
,'Bosnie-en-Herzegovina'
,'Botswana'
,'Brazilie'
,'Brits-Antarctisch-Territorium'
,'Brits-Indische-Oceaanterritorium'
,'Britse-Maagdeneilanden'
,'Brunei'
,'Bulgarije'
,'BurkinaFaso'
,'Burundi'
,'Cambodja'
,'Canada'
,'Centraal-Afrikaanse-Republiek'
,'Chili'
,'China'
,'Christmaseiland'
,'Cocoseilanden'
,'Colombia'
,'Comoren'
,'Congo-Brazzaville'
,'Congo-Kinshasa'
,'Cookeilanden'
,'CostaRica'
,'Cuba'
,'Curacao'
,'Cyprus'
,'Denemarken'
,'Djibouti'
,'Dominica'
,'Dominicaanse-Republiek'
,'Duitsland'
,'Ecuador'
,'Egypte'
,'ElSalvador'
,'Engeland'
,'Equatoriaal-Guinea'
,'Eritrea'
,'Estland'
,'Ethiopie'
,'Faeroer'
,'Falklandeilanden'
,'Fiji'
,'Filipijnen'
,'Finland'
,'Frankrijk'
,'Frans-Guyana'
,'Frans-Polynesie'
,'Gabon'
,'Gambia'
,'Georgie'
,'Ghana'
,'Gibraltar'
,'Grenada'
,'Griekenland'
,'Groenland'
,'Guadeloupe'
,'Guam'
,'Guatemala'
,'Guernsey'
,'Guinee'
,'Guinee-Bissau'
,'Guyana'
,'Haiti'
,'Honduras'
,'Hongarije'
,'HongKong'
,'Ierland'
,'India'
,'Indonesie'
,'Irak'
,'Iran'
,'Isle-of-Man'
,'Israel'
,'Italie'
,'Ivoorkust'
,'Jamaica'
,'Japan'
,'Jemen'
,'Jersey'
,'Jordanie'
,'Kaaimaneilanden'
,'Kaapverdie'
,'Kameroen'
,'Kazachstan'
,'Kenia'
,'Kirgizie'
,'Kiribati'
,'Koeweit'
,'Kosovo'
,'Kroatie'
,'Laos'
,'Lesotho'
,'Letland'
,'Libanon'
,'Liberia'
,'Libie'
,'Liechtenstein'
,'Litouwen'
,'Luxemburg'
,'Macau'
,'Macedonie'
,'Madagaskar'
,'Malawi'
,'Maldiven'
,'Maleisie'
,'Mali'
,'Malta'
,'Marokko'
,'Marshalleilanden'
,'Martinique'
,'Mauritanie'
,'Mauritius'
,'Mayotte'
,'Mexico'
,'Micronesia'
,'Moldavie'
,'Monaco'
,'Mongolie'
,'Montenegro'
,'Montserrat'
,'Mozambique'
,'Myanmar'
,'Namibie'
,'Nauru'
,'Nederland'
,'Nepal'
,'Nicaragua'
,'Nieuw-Caledonie'
,'NieuwZeeland'
,'Niger'
,'Nigeria'
,'Niue'
,'Noord-Ierland'
,'Noord-Korea'
,'Noordelijke-Marianen'
,'Noorwegen'
,'Norfolk'
,'Oeganda'
,'Oekraine'
,'Oezbekistan'
,'Oman'
,'Oost-Timor'
,'Oostenrijk'
,'Pakistan'
,'Palau'
,'PalestijnseGebieden'
,'Panama'
,'Papoea-Nieuw-Guinea'
,'Paraguay'
,'Peru'
,'Pitcairneilanden'
,'Polen'
,'Portugal'
,'PuertoRico'
,'Qatar'
,'Reunion'
,'Roemenie'
,'Rusland'
,'Rwanda'
,'Sao-Tome-en-Principe'
,'Saint-Barthelemy'
,'Saint-Kitts-en-Nevis'
,'Saint-Lucia'
,'Saint-Martin'
,'Saint-Pierre-en-Miquelon'
,'Saint-Vincent-en-de-Grenadines'
,'Salomonseilanden'
,'Samoa'
,'San-Marino'
,'Saudi-Arabie'
,'Schotland'
,'Senegal'
,'Servie'
,'Seychellen'
,'SierraLeone'
,'Singapore'
,'Sint-Maarten'
,'Slovenie'
,'Slowakije'
,'Soedan'
,'Somalie'
,'Akrotiri-en-Dhekelia'
,'Spanje'
,'Spitsbergen'
,'SriLanka'
,'Sint-Helena-Ascension-en-Tristan-da-Cunha'
,'Suriname'
,'Swaziland'
,'Syrie'
,'Tadzjikistan'
,'Taiwan'
,'Tanzania'
,'Thailand'
,'Togo'
,'Tokelau'
,'Tonga'
,'Trinidad-en-Tobago'
,'Tsjaad'
,'Tsjechie'
,'Tunesie'
,'Turkije'
,'Turkmenistan'
,'Turks-en-Caicoseilanden'
,'Tuvalu'
,'Uruguay'
,'Vaticaanstad'
,'Vanuatu'
,'Venezuela'
,'Verenigd-Koninkrijk'
,'Verenigde-Arabische-Emiraten'
,'Verenigde-Staten-van-Amerika'
,'Vietnam'
,'Wales'
,'Wallis-en-Futuna'
,'WestelijkeSahara'
,'Wit-Rusland'
,'IJsland'
,'Zambia'
,'Zimbabwe'
,'Zweden'
,'Zuid-Afrika'
,'Zuid-Georgie-en-de-Zuidelijke-Sandwicheilanden'
,'Zuid-Korea'
,'Zuid-Soedan'
,'Zwitserland']

british_islands = ['Anguilla', 'Bermuda', 'Brits-Antarctisch-Territorium', 'Brits-Indische-Oceaanterritorium', 'Britse-Maagdeneilanden', 'Falklandeilanden', 'Kaaimaneilanden', 'Montserrat', 'Pitcairneilanden', 'Akrotiri-en-Dhekelia', 'Sint-Helena-Ascension-en-Tristan-da-Cunha', 'Turks-en-Caicoseilanden','Zuid-Georgie-en-de-Zuidelijke-Sandwicheilanden']
french_islands = ['Mayotte', 'Saint-Barthelemy', 'Saint-Martin', 'Saint-Pierre-en-Miquelon']
countries_not_scraped = []
# countries = ['italie', 'griekenland']
for country in countries:

    if country in british_islands:
        ct = 'verenigd-koninkrijk/britse-overzeese-gebieden/' + country + '.htm'
    elif country in french_islands:
        ct = 'frankrijk/' + country + '.htm'
    else:
        ct = country
    page_link = 'http://www.klimaatinfo.nl/' + ct

    page_response = requests.get(page_link, timeout=5)

    soup = BeautifulSoup(page_response.content)

    tables = soup.find('table', {'id': 'AutoNumber3'})

    try:
        rows = tables.findChildren('tr')
    except:
        countries_not_scraped.append(country)
        continue
    rows = rows[2:14]

    COLUMN_NAMES = ['maand',
                    'gemiddelde max temperatuur',
                    'gemiddelde min temperatuur',
                    'zonuren',
                    'neerslagdagen',
                    'mm neerslag',
                    'zeetemperatuur']

    climate_table = pd.DataFrame(columns=range(0, 7), index = range(0,12))  # I know the size
    row_marker = 0
    for row in rows:
            column_marker = 0
            if (row_marker == 0) & (column_marker == 0):
                climate_table.iat[row_marker, column_marker] = 'month'
            columns = row.find_all('td')
            for column in columns:
                climate_table.iat[row_marker, column_marker] = column.get_text().rstrip().lstrip()
                column_marker += 1
            row_marker += 1
    climate_table.columns = COLUMN_NAMES
    properties = pd.DataFrame({'country': np.repeat(country, 8),
                               'period': ['zomer', 'winter', 'herfst', 'lente',
                                          'zomer', 'winter', 'herfst', 'lente'],
                               'properties': np.repeat(['temperatuur', 'zonuren'],4),
                               'values': None})

    zomer = ['juli', 'augustus', 'september']
    winter = ['januari', 'februari', 'maart']
    herfst = ['oktober', 'november', 'december']
    lente = ['april', 'mei', 'juni']

    properties.loc[(properties['period'] == 'zomer') & (properties['properties'] == 'temperatuur'), 'values'] = np.mean(climate_table.loc[climate_table['maand'].isin(zomer)]['gemiddelde max temperatuur'].values.astype(np.float))
    properties.loc[(properties['period'] == 'winter') & (properties['properties'] == 'temperatuur'), 'values'] = np.mean(climate_table.loc[climate_table['maand'].isin(winter)]['gemiddelde max temperatuur'].values.astype(np.float))
    properties.loc[(properties['period'] == 'herfst') & (properties['properties'] == 'temperatuur'), 'values'] = np.mean(climate_table.loc[climate_table['maand'].isin(herfst)]['gemiddelde max temperatuur'].values.astype(np.float))
    properties.loc[(properties['period'] == 'lente') & (properties['properties'] == 'temperatuur'), 'values'] = np.mean(climate_table.loc[climate_table['maand'].isin(lente)]['gemiddelde max temperatuur'].values.astype(np.float))

    properties.loc[(properties['period'] == 'zomer') & (properties['properties'] == 'zonuren'), 'values'] = np.mean(climate_table.loc[climate_table['maand'].isin(zomer)]['zonuren'].values.astype(np.float))
    properties.loc[(properties['period'] == 'winter') & (properties['properties'] == 'zonuren'), 'values'] = np.mean(climate_table.loc[climate_table['maand'].isin(winter)]['zonuren'].values.astype(np.float))
    properties.loc[(properties['period'] == 'herfst') & (properties['properties'] == 'zonuren'), 'values'] = np.mean(climate_table.loc[climate_table['maand'].isin(herfst)]['zonuren'].values.astype(np.float))
    properties.loc[(properties['period'] == 'lente') & (properties['properties'] == 'zonuren'), 'values'] = np.mean(climate_table.loc[climate_table['maand'].isin(lente)]['zonuren'].values.astype(np.float))
    print(country)
    properties_all_countries = properties_all_countries.append(properties)

print("hallo")
    # In my use case, I want to store the speech data I mentioned earlier.  so in this example, I loop through the paragraphs, and push them into an array so that I can manipulate and do fun stuff with the data.