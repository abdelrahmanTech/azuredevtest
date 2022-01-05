# Overview

<TODO: complete this with an overview of your project>

## Project Plan
    spreadsheet that includes the original and final project plan
    https://docs.google.com/spreadsheets/d/1RJ2WYgYxl-9pxpJa6-fiRI7Z6Cvg98SC/edit?usp=sharing&ouid=115967282947735842213&rtpof=true&sd=true

    Trello board for the project
    https://trello.com/b/xmUNdhBT

## Instructions

    Architectural Diagram Link (Shows how key parts of the system work
    Photo : https://drive.google.com/file/d/1kpa5oky1is7x4XN2WDV8DNe1-mlObRb1/view?usp=sharing
    Slide : https://docs.google.com/presentation/d/15W77rOWy4TE90R82Uc-Dah5uXIrTE33A/edit?usp=sharing&ouid=115967282947735842213&rtpof=true&sd=true

    <TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots>
    To run this project you have to follow below instructions in a sequence : 

    1- You have to clone the following repo into your github repo
    
        https://github.com/abdelrahmanTech/azuredevtest
    
    2- Open Azure Cloud Shell and make sure that you are using Bash and then setup connection between Azure cloud shell and github repo by follow the instructions in the following link
        https://www.youtube.com/watch?v=Z8uRw6N5TGY&t=84s

    3- Now you have to create Virtual Envirnoment by using the following command
        virtualenv ~/.mlazure

    4- And then type the following command to start using this virtual :
        source ~/.mlazure/bin/activate

    5- after that you need to clone your repo in Azure Cloud by using the following command
        git clone git@github.com:[YouGitHubAccount]/[RepoName].git

    6- you shoud have something like this in the following screenshot link
        https://drive.google.com/file/d/1dgAFmxbRNuiu77LtP_LPh3Td232GPxFV/view?usp=sharing

    7- after cloned successfully ,type the following command to change the directory into your cloned repo
        cd ./[your cloned repo folder]

    8- then type the following command and should passed as shown in below screenshot
        make all
        https://drive.google.com/file/d/17SZeqkqS1BWvCh3GkIYDyQIyf8LynbIr/view?usp=sharing

    9- once you confirmed that it's passed succssfully , then you have to create Azure App Service by using the following command
        az webapp u -n [your App Name]

    10- after createing Azure App Service , you can browse your application by using the following this and it should looks like the screenshot link
        https://<your-appservice>.azurewebsites.net/
        https://drive.google.com/file/d/1IbfzPUEbS1Aw6Cc-VtQBseQ07k7GScSl/view?usp=sharing

    11- now it's time to create azure devops by following the instructions listed in the following link
        https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops

    12- by acheiving previous step , the project is ready for use and you can see the following screenshots
    *  https://drive.google.com/file/d/1_Uu5-3RcS4adyIbOHu2dfglFs4GfZvfA/view?usp=sharing

    *  https://drive.google.com/file/d/1mltPZ7Nz8LY9X6vvTNqrkQkZqZyv-JKl/view?usp=sharing

    * Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

    * Running Azure App Service from Azure Pipelines automatic deployment

    * Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
    The output should look similar to this:

    ```bash
    udacity@Azure:~$ ./make_predict_azure_app.sh
    Port: 443
    {"prediction":[20.35373177134412]}
    ```

    * Output of streamed log files from deployed application



## Enhancements

<TODO: A short description of how to improve the project in the future>
I would like to enhance this project by integrate the list of data from live data source and expand the prediction to include more then one city

## Demo 

please watch this demo
https://www.youtube.com/watch?v=Dz-L-t7WQ3E




