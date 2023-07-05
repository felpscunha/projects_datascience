import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_combined_chart(df_final):
    '''
    Plots a combined chart showing the Weighted Average Retirement Savings Shortfall by Age Interval and Race,
    as well as the Retirement Readiness Rating by age interval.

    Parameters:
        df_final (DataFrame): The input DataFrame containing the relevant data.

    Returns:
        show combined charts
    '''
    def plot_retirement_savings_shortfall_chart(df_final):
        """
        Plots a chart showing the Weighted Average Retirement Savings Shortfall by Age Interval and Race.

        Parameters:
            df_final (DataFrame): The input DataFrame containing the relevant data.

        Returns:
            None
        """
        age_intervals = {'[35,39)': [35, 39], '[40,44)': [40, 44], '[45,49)': [45, 49], '[50,54)': [50, 54], '[55,59)': [55, 59], '[60,64)': [60, 64]}
        races = [1, 2, 3, 4]  

        # start of new df
        result_df = pd.DataFrame(columns=['Race', 'Interval', 'Weighted Average Retirement Savings Shortfall'])

        # "Retirement Savings Shortfall" calc by race and age (weighted average)
        for race in races:
            for interval, age_range in age_intervals.items():
                lower_age, upper_age = age_range
                subset = df_final[(df_final['race'] == race) & (df_final['initial_age'] >= lower_age) & (df_final['initial_age'] < upper_age)]
                total_count = len(subset)
                if total_count > 0:
                    weighted_sum_accumulated_capital = np.sum(subset.loc[subset['accumulated_capital'] < 0, 'accumulated_capital'] * subset.loc[subset['accumulated_capital'] < 0, 'weight'])
                    weighted_sum_new_accumulated_capital = np.sum(subset.loc[subset['new_accumulated_capital'] < 0, 'new_accumulated_capital'] * subset.loc[subset['new_accumulated_capital'] < 0, 'weight'])
                    total_weight = np.sum(subset['weight'])
                    weighted_average_shortfall = (weighted_sum_accumulated_capital + weighted_sum_new_accumulated_capital) / total_weight
                else:
                    weighted_average_shortfall = np.nan

                result_df = pd.concat([result_df, pd.DataFrame({
                    'Race': [race], 'Interval': [interval],
                    'Weighted Average Retirement Savings Shortfall': [abs(weighted_average_shortfall)]
                                                                })], ignore_index=True)

        # relationship the code with true labels
        result_df['Race'] = result_df['Race'].map({1: 'White', 2: 'Black', 3: 'Hispanic', 4: 'Other'})

        colors = sns.color_palette("colorblind", n_colors=len(result_df['Race'].unique()))

        # groupby data
        grouped_df = result_df.groupby(['Interval', 'Race'])['Weighted Average Retirement Savings Shortfall'].mean().unstack()

        # graph plot
        fig, ax = plt.subplots(figsize=(10, 6))
        grouped_df.plot(kind='bar', color=colors, ax=ax)
       
        plt.title('Weighted Average Retirement Savings Shortfall by Age Interval and Race', fontsize=16)
        plt.xlabel('Age Interval', fontsize=14)
        plt.ylabel('Weighted Average Retirement Savings Shortfall', fontsize=14)
        plt.legend(title='Race', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        plt.show()

    def calc_rrr(dataframe):
        """
        Calculates the Retirement Readiness Rating by age interval.

        Parameters:
            dataframe (DataFrame): The input DataFrame containing the relevant data.

        Returns:
            None
        """
        age_intervals = {'[35,39)': [35, 39], '[40,44)': [40, 44], '[45,49)': [45, 49],
                         '[50,54)': [50, 54], '[55,59)': [55, 59], '[60,64)': [60, 64]}
        accumulated_capital_percentages = []
        new_accumulated_capital_percentages = []

        for interval, age_range in age_intervals.items():
            lower_age, upper_age = age_range
            subset = dataframe[(dataframe['initial_age'] >= lower_age) & (dataframe['initial_age'] < upper_age)]
            total_count = len(subset)
            accumulated_capital_positive_count = len(subset[subset['accumulated_capital'] >= 0])
            new_accumulated_capital_positive_count = len(subset[subset['new_accumulated_capital'] >= 0])
            accumulated_capital_positive_percentage = (accumulated_capital_positive_count / total_count) * 100
            new_accumulated_capital_positive_percentage = (new_accumulated_capital_positive_count / total_count) * 100
            accumulated_capital_percentages.append(accumulated_capital_positive_percentage)
            new_accumulated_capital_percentages.append(new_accumulated_capital_positive_percentage)

        age_intervals = ['[35,39)', '[40,44)', '[45,49)', '[50,54)', '[55,59)', '[60,64)']

        # graph configs
        colors = sns.color_palette("colorblind", n_colors=2)
        bar_width = 0.35
        opacity = 0.8

        index = np.arange(len(age_intervals))
        plt.figure(figsize=(10, 6))
        plt.bar(index, accumulated_capital_percentages, bar_width, alpha=opacity, color=colors[0], label='Without Savers Match')
        plt.bar(index + bar_width, new_accumulated_capital_percentages, bar_width, alpha=opacity, color=colors[1], label='With Savers Match')

        # labels and ticks configs
        plt.xlabel('Age interval', fontsize=14)
        plt.ylabel('Retirement Readiness Rating (%)', fontsize=14)
        plt.title('Retirement Readiness Rating (%) by age interval', fontsize=16)
        plt.xticks(index + bar_width / 2, age_intervals, fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(title='Type', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)
        plt.tight_layout()
        plt.show()

    plot_retirement_savings_shortfall_chart(df_final)
    calc_rrr(df_final)