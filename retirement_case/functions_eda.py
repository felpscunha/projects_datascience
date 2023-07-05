def calculate_savers_match(income, family_kind, marital_status, annual_contribution, current_year):
    '''
    Calculates the Savers Match contribution for each contributor in the given DataFrame.
    The number of years of contribution will be taken into account with the retirement base of 65 years.
    Here it was assumed that: 
        - Single savers: family_kind == 1 and (marital_status == 4 or marital_status == 5)
        - Married couples filing jointly: family_kind == 1 and marital_status == 1
        - head-of-household filers: (family_kind == 2 or family_kind == 3) and (marital_status == 2 or marital_status == 3 or marital_status == 5)

    Args:
        dataframe (pandas.DataFrame): DataFrame containing taxpayer information.

    Returns:
        pandas.DataFrame: Updated DataFrame with 'total_saversmatch_contribution' column representing the total Savers Match contribution for each contributor.
    '''

    # Savers Match max_value 
    max_match = 0

    # retirement age
    retirement_age = 65

    # inflation 
    inflation = 0.044

    # savers match start year
    sm_start = 2027
       
    # inflation correction per year and adjusted income
    inflation_correction = (1+inflation) ** (current_year - sm_start)
    adjusted_income = income / inflation_correction

    # phase-out limits
    joint_lower_limit = 41000
    joint_upper_limit = 71000
    single_lower_limit = 20500
    single_upper_limit = 35500
    head_of_household_lower_limit = 30750
    head_of_household_upper_limit = 53250

    if family_kind == 1 and marital_status == 1:
        if adjusted_income < joint_lower_limit:
            max_match = 0.5 * 10000
        elif adjusted_income < joint_upper_limit:
            max_match = 0.5 * (10000) * (joint_upper_limit-adjusted_income)/(joint_upper_limit-joint_lower_limit)
        else:
            max_match = 0
    elif family_kind == 1 and (marital_status == 4 or marital_status == 5):
        if adjusted_income < single_lower_limit:
            max_match = 0.5 * 10000
        elif adjusted_income < single_upper_limit:
            max_match = 0.5 * (10000) * (single_upper_limit-adjusted_income)/(single_upper_limit-single_lower_limit)
        else:
            max_match = 0
    elif (family_kind == 2 or family_kind == 3) and (marital_status == 2 or marital_status == 3 or marital_status == 5):
        if adjusted_income < head_of_household_lower_limit:
            max_match = 0.5 * 10000
        elif adjusted_income < head_of_household_upper_limit:
            max_match = 0.5 * (10000) * (head_of_household_upper_limit-adjusted_income)/(head_of_household_upper_limit-head_of_household_lower_limit)
        else:
            max_match = 0
    
    # set savers match limit
    savers_match = min(annual_contribution * 0.5, max_match)

    return savers_match

def get_savers_match_benefit_total(dataframe, CURRENT_YEAR):
    # current year
    current_year = CURRENT_YEAR

    # retirement age
    retirement_age = 65

    # inflation 
    inflation = 0.044

    # savers match start year
    sm_start = 2027

    # savers match for each contributor
    for index, row in dataframe.iterrows():
        total_savers_match_contribution = 0
        income = row['income']
        family_kind = row['family_kind']
        marital_status = row['marital_status']
        annual_contribution = row['annual_contribution']
        initial_age = int(row["initial_age"])
        for age in range(initial_age, retirement_age + 1):
            if current_year >= sm_start:
                total_savers_match_contribution += calculate_savers_match(income, family_kind, marital_status,  income * annual_contribution, current_year)
            income *= (1+inflation)
            current_year += 1
        current_year = CURRENT_YEAR
       
        # total savers match contribution over the years
        dataframe.at[index, 'total_saversmatch_contribution'] = total_savers_match_contribution
    
    return dataframe