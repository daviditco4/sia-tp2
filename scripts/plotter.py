import glob
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import matplotlib.ticker as ticker

# Directory containing the CSV files
csv_directory = './outputs'

if __name__ == "__main__":
    # Get a list of all CSV files in the directory
    csv_files = glob.glob(os.path.join(csv_directory, '*.csv'))

    # Load each CSV file into a DataFrame and store them in a list
    dataframes = {os.path.splitext(os.path.basename(file))[0]: pd.read_csv(file) for file in csv_files}

    sns.set_theme()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['points_available'],
        x='PointsAvailable',
        y='ElapsedSeconds',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("elapsed_seconds_by_points_available_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    print('DID ONE')
    #
    # plt.figure()
    # # Use seaborn's lineplot with standard deviation bands
    # elapsed_seconds_plot = sns.barplot(
    #     data=dataframes['timeout'],
    #     x='ElapsedSecond',
    #     y='ElapsedSeconds',
    #     hue='CharacterClass',  # Color by algorithm
    #     errorbar=('sd', 2)
    # )
    # # Ensure x-axis labels are integers
    # elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    # plt.savefig("elapsed_seconds_by_timeout_barplot.png", dpi=300, bbox_inches='tight')
    # plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_population_size'],
        x='PopulationSize',
        y='ElapsedSeconds',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("elapsed_seconds_by_population_size_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_max_generations'],
        x='MaxGenerations',
        y='ElapsedSeconds',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("elapsed_seconds_by_max_generations_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_parents_selection'],
        x='ParentsSelection',
        y='ElapsedSeconds',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("elapsed_seconds_by_parents_selection_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_crossover'],
        x='Crossover',
        y='ElapsedSeconds',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("elapsed_seconds_by_crossover_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_mutation'],
        x='Mutation',
        y='ElapsedSeconds',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("elapsed_seconds_by_mutation_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_new_generation_selection'],
        x='NewGenerationSelection',
        y='ElapsedSeconds',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("elapsed_seconds_by_new_generation_selection_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['points_available'],
        x='PointsAvailable',
        y='SolutionScoreForEVE',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("solution_score_for_eve_by_points_available_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    # plt.figure()
    # # Use seaborn's lineplot with standard deviation bands
    # elapsed_seconds_plot = sns.barplot(
    #     data=dataframes['timeout'],
    #     x='Timeout',
    #     y='SolutionScoreForEVE',
    #     hue='CharacterClass',  # Color by algorithm
    #     errorbar=('sd', 2)
    # )
    # # Ensure x-axis labels are integers
    # elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    # plt.savefig("solution_score_for_eve_by_timeout_barplot.png", dpi=300, bbox_inches='tight')
    # plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_population_size'],
        x='PopulationSize',
        y='SolutionScoreForEVE',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("solution_score_for_eve_by_population_size_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_max_generations'],
        x='MaxGenerations',
        y='SolutionScoreForEVE',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("solution_score_for_eve_by_max_generations_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_parents_selection'],
        x='ParentsSelection',
        y='SolutionScoreForEVE',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("solution_score_for_eve_by_parents_selection_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_crossover'],
        x='Crossover',
        y='SolutionScoreForEVE',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("solution_score_for_eve_by_crossover_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_mutation'],
        x='Mutation',
        y='SolutionScoreForEVE',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("solution_score_for_eve_by_mutation_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()

    plt.figure()
    # Use seaborn's lineplot with standard deviation bands
    elapsed_seconds_plot = sns.barplot(
        data=dataframes['output_new_generation_selection'],
        x='NewGenerationSelection',
        y='SolutionScoreForEVE',
        hue='CharacterClass',  # Color by algorithm
        errorbar=('sd', 2)
    )
    # Ensure x-axis labels are integers
    elapsed_seconds_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.savefig("solution_score_for_eve_by_new_generation_selection_barplot.png", dpi=300, bbox_inches='tight')
    plt.close()
