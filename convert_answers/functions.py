import numpy as np

def check_qa(questions, answers):
    n_questions = len(questions)
    n_answers = len(answers)
    if n_answers != n_questions:
        print("ERROR: Number of questions asked not equal to number of answers given.")
        import sys
        sys.exit(1)
    return True

def subset_based_on_temperature(relevant_properties, questions, answers):
    try:
        temperature = answers[questions.index("temperatuur")]
    except:
        temperature = "onbelangrijk"

    if temperature == "warm":
        low = 20
        high = 100
    elif temperature == "koud":
        low = -100
        high = 5
    elif temperature == "onbelangrijk":
        low = -100
        high = 100

    temperature_properties = relevant_properties[relevant_properties["properties"] == "temperatuur"].copy()
    temperature_properties["values"] = temperature_properties["values"].apply(lambda x: float(x))
    countries = temperature_properties[(temperature_properties["values"] <= high) & (temperature_properties["values"] >= low)]["country"].values
    countries = np.unique(countries)
    return countries

def subset_based_on_sun(relevant_properties, questions, answers):
    try:
        sun = answers[questions.index("zon")]
        sun_threshold = 7.5
        sun_properties = relevant_properties[relevant_properties["properties"] == "zonuren"].copy()
        sun_properties["values"] = sun_properties["values"].apply(lambda x: float(x))
        if sun == "ja":
            countries = sun_properties[sun_properties["values"] >= sun_threshold]["country"].values
            countries = np.unique(countries)

        else:
            countries = np.unique(relevant_properties["country"])
    except:
        countries = np.unique(relevant_properties["country"])
    return countries

def subset_based_on_budget(relevant_properties, questions, answers):
    try:
        budget = answers[questions.index("budget")]
    except:
        budget = "hoog"

    budget_properties = relevant_properties[relevant_properties["properties"] == "budget"].copy()

    if budget == "hoog":
        # IF BUDGET = "hoog" --> SELECT BUDGET = "gemiddeld" AND BUDGET == "hoog"
        countries = budget_properties[~budget_properties["values"].isin(["laag"])]["country"].values
    elif budget == "gemiddeld":
        # IF BUDGET = "gemiddeld" --> SELECT BUDGET = "gemiddeld" AND BUDGET == "laag"
        countries = budget_properties[~budget_properties["values"].isin(["hoog"])]["country"].values
    elif budget == "laag":
        # IF BUDGET = "laag" --> SELECT BUDGET == "laag"
        countries = budget_properties[budget_properties["values"].isin(["laag"])]["country"].values

    countries = np.unique(countries)
    return countries

def subset_based_on_transport(relevant_properties, questions, answers):
    try:
        transport = answers[questions.index("vervoersmiddel")]
        if transport != "onbelangrijk":
            transport_properties = relevant_properties[relevant_properties["properties"] == "vervoersmiddel"].copy()
            countries = transport_properties[transport_properties['values'].str.contains(transport)]['country'].values
            countries = np.unique(countries)
        else:
            countries = np.unique(relevant_properties["country"])
    except:
        countries = np.unique(relevant_properties["country"])

    return countries

def subset_based_on_water(relevant_properties, questions, answers):
    try:
        water = answers[questions.index("water")]
        if water != "onbelangrijk":
            water_properties = relevant_properties[relevant_properties["properties"] == "water"].copy()
            countries = water_properties[water_properties['values'].str.contains(water)]['country'].values
            countries = np.unique(countries)
        else:
            countries = np.unique(relevant_properties["country"])

    except:
        countries = np.unique(relevant_properties["country"])

    return countries

def subset_based_on_continent(relevant_properties, questions, answers):
    try:
        continent = answers[questions.index("continent")]
        if continent != "onbelangrijk":
            countries = relevant_properties[relevant_properties['continent'].str.contains(continent)]['country'].values
            countries = np.unique(countries)
        else:
            countries = np.unique(relevant_properties["country"])

    except:
        countries = np.unique(relevant_properties["country"])

    return countries

def subset_based_on_continent_europa(relevant_properties, questions, answers):
    try:
        continent_europa = answers[questions.index("continent_europa")]
        if continent_europa != "onbelangrijk":
            if continent_europa == 'buiten':
                countries = relevant_properties[relevant_properties['continent'].str.contains("azie|oceanie|afrika|midden amerika|noord amerika|zuid amerika")]['country'].values
                countries = np.unique(countries)
            else:
                countries = relevant_properties[relevant_properties['continent'].str.contains("europa")]['country'].values
        else:
            countries = np.unique(relevant_properties["country"])

    except:
        countries = np.unique(relevant_properties["country"])

    return np.unique(countries)

def subset_based_on_culture(relevant_properties, questions, answers):
    try:
        culture = answers[questions.index("cultureel")]
        if culture == "ja":
            culture_properties = relevant_properties[relevant_properties["properties"] == "cultureel"].copy()
            countries = culture_properties[culture_properties['values'].str.contains(culture)]['country'].values
            countries = np.unique(countries)
        else:
            countries = np.unique(relevant_properties["country"])

    except:
        countries = np.unique(relevant_properties["country"])

    return countries

def subset_based_on_adventure(relevant_properties, questions, answers):
    try:
        adventure = answers[questions.index("avontuurlijk")]
        if adventure == "ja":
            adventure_properties = relevant_properties[relevant_properties["properties"] == "avontuurlijk"].copy()
            countries = adventure_properties[adventure_properties['values'].str.contains(adventure)]['country'].values
            countries = np.unique(countries)
        else:
            countries = np.unique(relevant_properties["country"])

    except:
        countries = np.unique(relevant_properties["country"])

    return countries