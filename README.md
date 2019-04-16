# Hackacity 2019


Repo for the work presented at Hackacity 2019, which led to a 2nd Prize on the competition 🏆.

# Problem and Goals
 * Use regression techniques to uncover what makes local housing (Alojamento Local) locations be valued by customers and entrepreneurs so that the municipality can better understand how to approach the overflow of local housing problem and how to influence its evolution overtime.
 * Detect local housing establishments on booking.com that are not listed in the official municipality dataset, a helping hand in finding illegal establishments.


# Data Science Pipeline
 * Implement interaction with Porto's APIs - [01_api_interaction.ipynb](01_api_interaction.ipynb)
    * These functions (and some more) have been extracted into an importable file - [dataset_bending.py](dataset_bending.py) and there are tests and use cases available in [some_tests.ipynb](some_tests.ipynb) and the complete listing of datasets and sub-datasets available in the APIs is available at [sub_datasets.ipynb](sub_datasets.ipynb)
	* Some useful functions to inspect and handle geographical data have also been implemented - [geographical_functions.ipynb](geographical_functions.ipynb) they have also been isolated to the [geographical_functions.py](geographical_functions.py) file
 * Merge the local housing dataset with the data scrapped from booking.com - [02_dataset_building.ipynb](02_dataset_building.ipynb)
    * The 'scraping' of booking (with no financial goal) has been implemented in [booking_scrapping.py](booking_scrapping.py) and some helper functions for this are present in [booking_parsing.ipynb](booking_parsing.ipynb)
 * Feature engineering from more geographical datasets into the main local housing dataset (green spaces, access to metro, bus, ...) - [03_feature_engineering.ipynb](03_feature_engineering.ipynb)
 * Merge the feature engineering dataset with the local housing dataset - [04_merge_with_features.ipynb](04_merge_with_features.ipynb)
 * Analysis of the built datasets, clustering, regression 
    * [05_dataset_analysis.ipynb](05_dataset_analysis.ipynb)
	* [05_dataset_analysis_02.ipynb](05_dataset_analysis_02.ipynb)

# Datasets
A script to download all the datasets is available in [download_all.ipynb](download_all.ipynb) and the remaining data is available on the [datasets/](datasets/) folder. 

The temporary datasets that were built and used during the competition are available in the [generated_datasets/](generated_datasets/) folder (Initially they were in the root folder and the notebooks still expect that).

