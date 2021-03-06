import convert_answers.functions as ca
import random
import pickle
import pandas as pd
import matplotlib.pyplot as plt

def determineChoice(questions, answers):
    activity = answers[questions.index("activiteit")]

    if activity == "strand":
        questions.append("temperatuur")
        answers.append("warm")

        questions.append("zon")
        answers.append("ja")

        questions.append("strandvakantie")
        answers.append("ja")

    if activity == "avontuur":
        questions.append("avontuurlijk")
        answers.append("ja")

    ca.check_qa(questions, answers)

    properties = pickle.load(open('data_properties.pkl', 'rb'))
    qa = pickle.load(open('data_qa.pkl', 'rb'))

    ## FIGURE OUT WHICH PERIOD (IF ASKED)
    try:
        period = answers[questions.index("periode")]
        period = [period]
        period.append("")
    except:
        period = ["zomer", "winter", "herfst", "lente", ""]

    relevant_properties = properties[properties["period"].isin(period)]

    ## TEMPERATURE SUBSET
    countries = ca.subset_based_on_temperature(relevant_properties, questions, answers)
    relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]

    ## SUN SUBSET
    countries = ca.subset_based_on_sun(relevant_properties, questions, answers)
    relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]

    # ## BUDGET SUBSET
    # countries = ca.subset_based_on_budget(relevant_properties, questions, answers)
    # relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]
    #
    # ## MEANS OF TRANSPORT SUBSET
    # countries = ca.subset_based_on_transport(relevant_properties, questions, answers)
    # relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]
    #
    # ## WATER SUBSET
    # countries = ca.subset_based_on_water(relevant_properties, questions, answers)
    # relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]

    ## BEACH SUBSET
    countries = ca.subset_based_on_beach(relevant_properties, questions, answers)
    relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]
    #
    # ## CONTINENT SUBSET
    # countries = ca.subset_based_on_continent(relevant_properties, questions, answers)
    # relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]

    ## CONTINENT EUROPA SUBSET
    countries = ca.subset_based_on_continent_europa(relevant_properties, questions, answers)
    relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]

    ## CULTURAL SUBSET
    countries = ca.subset_based_on_culture(relevant_properties, questions, answers)
    relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]

    ## ADVENTURE SUBSET
    countries = ca.subset_based_on_adventure(relevant_properties, questions, answers)
    relevant_properties = relevant_properties[relevant_properties["country"].isin(countries)]
    if len(countries) > 0:
        recommended_country = random.choice(countries)
    else:
        recommended_country = "GEEN LAND MOGELIJK"
    print(countries)
    print(len(countries))

    return recommended_country

if __name__ == '__main__':
    all_answer_combinations = [[a, b, c, d] for a in ["winter", "zomer", "herfst", "lente"] for b in ["binnen", "buiten"] for c in ["avontuur", "strand"] for d in ["ja", "nee"]]
    for answer in all_answer_combinations:
        print(answer)
        determineChoice(["periode","continent_europa","activiteit","cultureel"],answer)


