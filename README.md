# Overview
The purpose of this project to show you how to build continuosly integrate and continuosly deliver your code by using GitHub Actions and Azure DevOps,
where you will comprehinsive insight of how to build CI/CD pipeline, the below link of the Architecture Diagram shows the complete cycle of the process in the CI/CD Context

https://drive.google.com/file/d/1kpa5oky1is7x4XN2WDV8DNe1-mlObRb1/view?usp=sharing

<TODO: complete this with an overview of your project>

## Project Plan
    spreadsheet that includes the original and final project plan
        https://docs.google.com/spreadsheets/d/1RJ2WYgYxl-9pxpJa6-fiRI7Z6Cvg98SC/edit?usp=sharing&ouid=115967282947735842213&rtpof=true&sd=true

    Trello board for the project
        https://trello.com/b/xmUNdhBT

    Architecture Diagram
        https://drive.google.com/file/d/1kpa5oky1is7x4XN2WDV8DNe1-mlObRb1/view?usp=sharing
    
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
	see below screenshots
	- setup SSH key in GitHub
		https://drive.google.com/file/d/1PHPt79rrWMXZvwTxspfYIqVCD0LzKdwF/view?usp=sharing

    3- Now you have to create Virtual Envirnoment by using the following command
        virtualenv ~/.mlazure

    4- And then type the following command to start using this virtual :
        source ~/.mlazure/bin/activate

    5- after that you need to clone your repo in Azure Cloud by using the following command
        git clone git@github.com:[YouGitHubAccount]/[RepoName].git
	
    6- the cloned repo in azure looks like this in the following screenshot link
        https://drive.google.com/file/d/1dgAFmxbRNuiu77LtP_LPh3Td232GPxFV/view?usp=sharing

    7- after cloned successfully ,type the following command to change the directory into your cloned repo
        cd ./[your cloned repo folder]

    8- then type the following command and should passed as shown in below screenshot
        make all
        make all screenshot : https://drive.google.com/file/d/17SZeqkqS1BWvCh3GkIYDyQIyf8LynbIr/view?usp=sharing

    9- once you confirmed that it's passed succssfully , then you have to create Azure App Service by using the following command
        az webapp u -n [your App Name]

    10- after createing Azure App Service , you can browse your application by using the following this and it should looks like the screenshot link
        https://<your-appservice>.azurewebsites.net/

        Web App Screenshot : https://drive.google.com/file/d/1IbfzPUEbS1Aw6Cc-VtQBseQ07k7GScSl/view?usp=sharing

    11- now it's time to create azure devops by following the instructions listed in the following link
        https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops

    
	# Continuous Integration

	* Screenshot showing the project cloned into Azure Cloud Shell.
		 https://drive.google.com/file/d/1dgAFmxbRNuiu77LtP_LPh3Td232GPxFV/view?usp=sharing
	* Screenshot showing the passing tests that are displayed after running the make all command from the Makefile
		https://drive.google.com/file/d/17SZeqkqS1BWvCh3GkIYDyQIyf8LynbIr/view?usp=sharing
	* Screebshot Python GitHub Action Test Result
		https://drive.google.com/file/d/1GJRgipe9UtSD_KTdJhQj18tFyD83wpqo/view?usp=sharing
	* GitHub Action YAML file location in repo
		https://github.com/abdelrahmanTech/azuredevtest/blob/main/.github/workflows/main.yml
    * GitHub Action Badge
	
	#Continuous Delivery
    * A screenshot of Azure Azure App Service
        https://drive.google.com/file/d/1IbfzPUEbS1Aw6Cc-VtQBseQ07k7GScSl/view?usp=sharing
        https://drive.google.com/file/d/1fXMTswudxpaPCpt9f6socDx-UUxC-lOL/view?usp=sharing
    * A screenshot of a successful prediction in Azure Cloud Shell
        https://drive.google.com/file/d/1mltPZ7Nz8LY9X6vvTNqrkQkZqZyv-JKl/view?usp=sharing
    * screenshot of the application running against a load test with locust
        screenshot 1 : https://drive.google.com/file/d/1L50y1xgO9dlMZTFtDdWKOJmPJ9hgoW2G/view?usp=sharing
        screenshot 2 : https://drive.google.com/file/d/15lto8Wx4cpkzf_VTIS7Gbg0C9dN3n8Ea/view?usp=sharing
    * screenshot of a successful run of the project in Azure Pipelines
        https://drive.google.com/file/d/1jwJE4RmARdUO1E_w4LMaZDl1jSfJo5xg/view?usp=sharing

    * Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

    * Running Azure App Service from Azure Pipelines automatic deployment
        https://drive.google.com/file/d/1_Uu5-3RcS4adyIbOHu2dfglFs4GfZvfA/view?usp=sharing

    * Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
    The output should look similar to this:

    ```bash
    udacity@Azure:~$ ./make_predict_azure_app.sh
    Port: 443
    {"prediction":[20.35373177134412]}
    ```
	    https://drive.google.com/file/d/1mltPZ7Nz8LY9X6vvTNqrkQkZqZyv-JKl/view?usp=sharing

    * Output of streamed log files from deployed application
        [{"machineName":"pl0sdlwk00002H_default","lastUpdated":"2022-01-07T03:35:45.8284311Z","size":1496762,"href":"https://mlazurewebap.scm.azurewebsites.net/api/vfs/LogFiles/2022_01_07_pl0sdlwk00002H_default_docker.log","path":"/home/LogFiles/2022_01_07_pl0sdlwk00002H_default_docker.log"},{"machineName":"pl0sdlwk00002H","lastUpdated":"2022-01-05T18:38:19.6224215Z","size":2130,"href":"https://mlazurewebap.scm.azurewebsites.net/api/vfs/LogFiles/2022_01_05_pl0sdlwk00002H_docker.log","path":"/home/LogFiles/2022_01_05_pl0sdlwk00002H_docker.log"}]
	

## Enhancements

<TODO: A short description of how to improve the project in the future>

	I would like to enhance this project by integrate the list of data from live data source and expand the prediction to include more than one city and also improve the deployment to make it more durable by using kubernetes cluster and in such senario i want to confirm that the application deployed successfully or i should make roll back to ensure there will not be intrupt on the service 

## Demo 

please watch this demo
https://www.youtube.com/watch?v=Dz-L-t7WQ3E


##GitHuub Actions Badge
[![Python application test with Github Actions](https://github.com/abdelrahmanTech/azuredevtest/actions/workflows/main.yml/badge.svg)](https://github.com/abdelrahmanTech/azuredevtest/actions/workflows/main.yml)
