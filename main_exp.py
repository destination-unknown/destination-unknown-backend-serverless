import convert_answers_exp.functions as ca
import random
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None  # default='warn'

def determineChoice(questions, answers):
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
    relevant_properties = ca.subset_based_on_temperature(relevant_properties, questions, answers)

    ## GOAL SUBSET
    relevant_properties = ca.subset_based_on_goal(relevant_properties, questions, answers)

    ## ETA SUBSET
    relevant_properties = ca.subset_based_on_eta(relevant_properties, questions, answers)

    ## MEANS OF ACTIVITIES SUBSET
    relevant_properties_sorted = ca.subset_based_on_activities(relevant_properties, questions, answers)

    countries_sorted = relevant_properties_sorted['country']
    if len(countries_sorted) == 0:
        countries_sorted = "GEEN LAND MOGELIJK"

    return np.array(countries_sorted).tolist()

if __name__ == '__main__':
    # all_answer_combinations = [[a, b, c, d, e] for a in ["winter", "zomer", "herfst", "lente"] for b in ["tot rust komen", "op avontuur gaan"] for c in ["4","8","12","24"] for d in ["15","20","25","30","-99"] for e in ["hiken|cultuur snuiven|wintersporten|rondreizen|watersporten|op het strand liggen|stadjes bezoeken"]]
    # i = 0
    # c = 0
    # for answer in all_answer_combinations:
    #     i = i + 1
    #     print(answer)
    #     x = determineChoice(["periode","doel","lengte reis","temperatuur", "activiteit"],
    #                         answer)
    #     if len(x) > 0:
    #         c = c + 1

    determineChoice(["periode","doel","lengte reis","temperatuur", "activiteit"],
                    ["zomer", "tot rust komen", "24", "15","hiken|watersporten|wintersporten"])

    # print(i)
    # print(c)
