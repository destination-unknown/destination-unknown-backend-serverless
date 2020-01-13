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
        temperature = float(answers[questions.index("temperatuur")])
    except:
        temperature = float(-99)

    relevant_properties["temperatuur"] = relevant_properties["temperatuur"].astype(float)
    relevant_properties = relevant_properties[relevant_properties["temperatuur"] >= temperature]
    return relevant_properties

def subset_based_on_goal(relevant_properties, questions, answers):
    try:
        goal = answers[questions.index("doel")]
        relevant_properties = relevant_properties[relevant_properties[goal] == '1'].copy()
    except:
        relevant_properties = relevant_properties
    return relevant_properties

def subset_based_on_eta(relevant_properties, questions, answers):
    try:
        eta = float(answers[questions.index("lengte reis")])
    except:
        eta = float(24)

    relevant_properties["uren onderweg"] = relevant_properties["uren onderweg"].str.replace(',', '.').astype(float)
    relevant_properties = relevant_properties[relevant_properties["uren onderweg"] <= eta]
    return relevant_properties


def subset_based_on_activities(relevant_properties, questions, answers):
    relevant_properties[['hiken in de bergen',
                         'cultuur snuiven',
                         'wintersporten',
                         'rondreizen',
                         'watersporten',
                         'op het strand liggen',
                         'stadjes bezoeken']] = relevant_properties[['hiken in de bergen',
                                                                     'cultuur snuiven',
                                                                     'wintersporten',
                                                                     'rondreizen',
                                                                     'watersporten',
                                                                     'op het strand liggen',
                                                                     'stadjes bezoeken']].astype(int)
    column_subset = ["country"]

    try:
        activities = answers[questions.index("activiteit")]
        if "hiken" in activities:
            column_subset.append("hiken in de bergen")
        if "cultuur snuiven" in activities:
            column_subset.append("cultuur snuiven")
        if "wintersporten" in activities:
            column_subset.append("wintersporten")
        if "rondreizen" in activities:
            column_subset.append("rondreizen")
        if "watersporten" in activities:
            column_subset.append("watersporten")
        if "op het strand liggen" in activities:
            column_subset.append("op het strand liggen")
        if "stadjes bezoeken" in activities:
            column_subset.append("stadjes bezoeken")

        activities_summary = relevant_properties[column_subset].copy()
        relevant_properties['sum'] = activities_summary.sum(1)
        relevant_properties_shuffled = relevant_properties.sample(frac=1)
        relevant_properties_sorted = relevant_properties_shuffled.sort_values(by='sum', ascending=False)
    except:
        relevant_properties_sorted = relevant_properties.sample(frac=1)

    return relevant_properties_sorted
