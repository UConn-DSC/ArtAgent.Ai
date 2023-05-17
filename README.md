# ArtAgent.Ai

## Purpose
We are proud to introduce ArtAgent.Ai: the inaugural open-source project by UConn Data Science Club. ArtAgent.Ai is a cutting-edge tool meticulously crafted for Visual Artists, harnessing the power of machine learning to guide users towards the most engaging online communities for their work. By embracing data-driven decision-making, ArtAgent.Ai empowers users to discover their artistic niche, amplify their popularity, and ultimately cultivate a sustainable income through commissioned projects that stem from their heightened visibility.

## Background
During HackUConn 2023, a team from UConn Data Science Club consisting of Pranav Tavildar, Alex McLeod, Sai Akavaramu, Jeffrey Chen, and Ankith Nagabandi initiated the development of this project. The first version of ArtAgent.AI was conceptualized, developed, trained, and tested over a an intense period of 20 hours. The tool employs web scraping techniques to extract image files from the trending section of the most popular art subreddits. Additionally, it harnesses the capabilities of a Convolutional Neural Network (CNN) to process inputs and intelligently recommend the subreddits with the most closely aligned content.

## Current Plans
- Expand our data sets and models
  - Develop a methodology to scrape the latest images from online communities periodically and fine tune the model. 
- Improve UX and functionality
  - Create a front-end userface using React.js, in the future possibly adding support for user accounts.
- Collaborate with the UConn Artists
  - Take feedback from users and UConn Fine Arts department to make modifications.


## File Overview
- .gitignore specifies which files are tracked when making commits and pushing code.
- CONTRIBUTING.md specifies guidelines for making contributions to this open source project.
- LICENSE contains legal permissions granted to users, allowing them to access, modify, and distribute software's source code freely. We use the Open Source MIT license
- artpilot.jpg is the logo of ArtAgent.Ai
- artpilot.trans is a transparent version of the logo
- interface.py is a simple front-end interface that takes in the path of an image and uses the model to make predictions.
- processing.py contains all the data cleaning and processing as well as model training and evaluation.
- (missing) scraping.py contains the code which was used to scrape images from various subreddits.
- reddit_model.pth this file is a pretrained CNN model that is used in the current version to make predictions. This file is accessible in the releases section under the model tag.
