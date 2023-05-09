
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
# Welcome to the Pokemoon Repository !
<br />
<div align="center">
  <a href="https://github.com/ianzhg/Pokemon">
    <img src="pokemoon.jpeg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Pokemon-README</h3>

  <p align="center">
    An awesome application to find the better you!
    <br />
    <a href="https://github.com/ianzhg/Pokemon"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://doit-oose.herokuapp.com/">View Demo</a> -->
    ·
    <a href="https://github.com/ianzhg/Pokemon/issues">Report Bug</a>
    ·
    <a href="https://github.com/ianzhg/Pokemon/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<br>

<!-- !![landing](https://i.imgur.com/uDFA0cd.png) -->

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This repository contains a Pokemon application designed to track and compare the price differences between the Japan and US markets for Pokemon cards. This tool is especially useful for collectors and resellers looking to take advantage of price discrepancies across markets.

 - Track and compare Pokemon card prices between the Japan and US markets.
 - Identify profitable opportunities for buying and selling cards across markets.
 - Fetch real-time card prices from trusted sources.
 - Keep track of price trends and fluctuations over time.

<!-- Here's why:
* People often feel unmotivated and discouraged to do academic, professional, and personal tasks. :sob:
* There currently are only to-do list applications that allow you to list and plan the tasks that you need to complete. 
* The market is lacking a solution that focuses on actually pushing users to actually do the tasks! DoIt is our solution to these problems. :relaxed:

Through the betting system in Dolt, users need a certain amount of Dolt coins to play the game. Users can set private tasks for themselves or set tasks for everyone in a group. For group tasks, other people can keep track of them by verifying their posts in the group chat. The user who fails to do their tasks will lose DoIt coins and the rest of the users will spilt the coins evenly. Successful users will be able to help friends gain better habits, get tasks done, earn more DoIt coins along the way, and have the opportunity to upload content to group chats to communicate with friends. People are motivated more by losses than by gains, so we want to motivate people by introducing consequences of having DoIt coins on the line. We also allow users to be motivated by recognition in the group chat and by gaining group coins when they complete tasks. -->

<!-- Types of Coins:
* Free coins (Users start out with some coins upon registration)
* In the future, we may choose to include paid coins; however, the DoIt app only offers free coins at this time.

The existence of free coins allows users to complete tasks under the supervision of others (and face possible consequences of losing DoIt coins) while enjoying the fun of gaining community recognition and rewards when friends fail to do tasks. -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Here are major frameworks/libraries we used to build our project.
* [![React][React.js]][React-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![MongoDB][MongoDB.com]][MongoDB-url]
* [![MaterialUI][mui.com]][mui-url]
* ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
<!-- * [![Axios][axios-http.com]][axios-http-url]
* [![getstream][getstream-http.com]][getstream-http-url]
* [![heroku][heroku-http.com]][heroku-http-url]
* [![Node.js][Node.js.com]][Node.js-url]
* [![Express][Express.com]][Express-url] -->


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

<!-- View a deployed version of our website here: https://doit-oose.herokuapp.com/ -->

### Installation

1. Navigate to the ```backend``` folder 
    ```sh
    cd backend
    ```
    Then 
    ```sh
    pip install -r requirements.txt
    ```
    to install all dependencies

2. Next run the following code to set up the virtual environment for backend

    - for window:
        ```sh
        python -m venv venv
        ```
    - for mac
        ```sh
        python3 -m venv venv
        ```
    
    - Then run 
        ```sh
        python app.py
        ```
3. Navigate to the ```frontend``` folder 
    ```sh
    cd frontend
    ```
    Then run
    ```sh
    npm i --force
    ```
    to install all dependencies. 
   
4. Run the following code to start the frontend
    ```sh
    npm run start
    ```
5. You should be directed to ```http://localhost:3000/```




# Achievements
- One of our key strengths is our ability to consolidate information from disparate sources and derive meaningful insights. In our code, we integrate information from multiple websites, across two different languages, and across various types of data including card pricing, exchange rates, and shipping information to identify arbitrage opportunities. Each section of the code has a moderate scope and complexity but combined together provides value for our users.

- Our code is a scalable and efficient solution for collecting and monitoring pricing and card information for Pokemon cards from multiple pages of Japanese and US trading websites. We utilize Beautiful Soup and regular expressions to accurately extract relevant information, ensuring consistent and reliable data. The structure of our code is clear and we can easily scale it to more regions, languages, and currencies.

- Our code allows users to compare shipping prices from three different shipping companies: Japan Post, DHL, and FedEx. By entering the required information, such as the number of cards, US zip code, and Japan zip code, users can easily view shipping prices and options from each company. Please note that due to the use of Selenium scripts, fetching the results may take approximately 15-30 seconds per shipping company. Link

- Our code allows users to easily convert currencies between USD and JPY. You can always click on the money icon to access the currency conversion tool via a pop-up window. Link

- Our code effectively extracts US card names and prices for Pokémon cards using BeautifulSoup and Selenium. This is a significant achievement, considering the complexities involved in dealing with different languages, text formats, and website structures. By using both Selenium and Beautiful Soup, we have ensured a robust and flexible approach to data extraction that can handle various challenges and adapt to future changes in website structures. Link Link

- We successfully identified 1,000 cards with valid US prices out of 5,000 cards with JP names and JP prices. This high extraction rate speaks to the quality and effectiveness of our code, especially given the challenges of dealing with differences in text, languages, and cultures between the two countries. Link  Link

- Despite time constraints, we have developed a fully functional frontend interface that is both user-friendly and visually reasonable. By leveraging multiple libraries and technologies, we have created a decent experience for users to navigate with our websites and learn the price differences between JP and US cards. Link

- We have incorporated a cart feature that allows users to compare the total price of their selected cards in both US dollars and Japanese yen. This feature allows users to make informed decisions about their purchases by offering a clear and straightforward way to assess potential cost savings or earnings. Link

# Limitations and Possible Improvements
- When scraping Japanese and US card prices, the solution is customized to the particular card trading websites. To extract data from more websites, we will need to build customizable scarping solutions for those websites as well and the marginal return is low. However, since most of the trading websites follow a similar structure in presenting information (name, id, and price), a possible improvement is to use machine learning techniques and automatically find the prices instead of customizing our code for each website. The complexity of the solution might be high since we need to make a universal solution for different websites but we could greatly increase the reliability of the prices since it comes from more sources.

- When attempting to obtain shipping prices from FedEx, USPS, UPS, and DHL, we encountered difficulties using their APIs directly. To access the APIs for FedEx, USPS, and DHL, a business API key is required, which necessitates having an actual company and applying for it. As for UPS, their API only permits quoting shipping prices from the US to Japan, rather than from Japan to the US. Consequently, we decided to utilize Selenium scripts to perform GUI interactions directly on the respective websites.
  - This approach results in longer delays, taking approximately 15-30 seconds per shipping company.
  - The Selenium script may occasionally time out, requiring users to rerun the function on the webpage.
  - When running Selenium, a pop-up window appears. Although I attempted to use "headless" mode to mitigate this issue, it increased the likelihood of encountering bugs.

- As our website is not yet deployed, we are unable to implement automated crawling functionality that would allow for regular updates, such as hourly or daily refreshes of card prices and information. This limitation impacts the real-time accuracy of our data. After the finals, we plan to deploy the website and enhance the crawling functionality for more up-to-date information.

- Currently, our project focuses on a select number of websites that sell Pokémon cards. However, not all cards are available on these sites, which may limit the comprehensiveness of our platform. In the future, we plan to incorporate more websites into our data collection process to improve our market coverage and offer a more comprehensive service to our users.

- Our current implementation relies on Beautiful Soup to scrape card information, which requires making an HTTP request for each card individually. This approach can be slow and resource-intensive, especially when dealing with a large number of cards. We are exploring alternative methods for data collection that can improve the efficiency of our scraping process without compromising the quality of our data.

- Our project relies on the accuracy and availability of data from third-party websites, which may change their structure, policies, or availability at any time. This dependency presents a risk to the stability of our platform, and we will need to continually monitor and adapt to changes in these sources to maintain the accuracy and reliability of our data.


<!-- USAGE EXAMPLES -->
## Usage
![Shipping Page](https://i.imgur.com/tjku0c8.png)
- This page allows users to compare shipping prices from three different shipping companies: Japan Post, DHL, and FedEx. By entering the required information, such as the number of cards, US zip code, and Japan zip code, users can easily view shipping prices and options from each company. Please note that due to the use of Selenium scripts, fetching the results may take approximately 15-30 seconds per shipping company.

![Currency Page](https://i.imgur.com/xvWqyMR.png)
- This page allows users to easily convert currencies between USD and JPY. You can always click on the money icon to access the currency conversion tool via a pop-up window.




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the development community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork this repo and create a pull request. Please feel free to reach out to one of the Team DoIt Members below via email to contact us, too! We'd love to talk.

Don't forget to give the project a star! :star: Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b`)
3. Commit your Changes (`git commit -m 'RandomMessage'`)
4. Push to the Branch (`git push origin`)
5. Open a Pull Request

<!-- ### Steps to Run Locally
1. Run `npm run install-all` to install all dependencies for both the frontend and backend
2. `cd` into `server` folder, then run `node index.js` to start the server on port 5000
3. In a new terminal, `cd` into the `frontend` folder and run `npm start` to start the frontend on port 3000

Note: To switch between using the Heroku backend and the local backend, change the URL in the `frontend/src/axiosSettings.js` file to the URL of the backend you want to use.
For example, if you want to use the Heroku backend, change the URL to `https://backend-oose-doit.herokuapp.com/`
For example, if you want to use the local backend, change the URL to `http://localhost:5000/` -->



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

### Pokemon Project Members (listed in alphabetical order):


- Yujian (Ken) He - [@Kennnnn774](https://github.com/Kennnnn774) - yhe99@jhu.edu
- Shaopeng Zeng - [@SP-Zeng](https://github.com/SP-Zeng) - szeng10@jhu.edu
- Ian Zheng - [@ianzhg](https://github.com/ianzhg) - yzheng67@jhu.edu

<!-- Project Link: [https://github.com/jhu-oose-f22/team-doit-project-repo](https://github.com/jhu-oose-f22/team-doit-project-repo) -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

We are thankful for these resources which have helped us on our development journey:

* [Choose an Open Source License](https://choosealicense.com)
* [Material UI](https://mui.com)
* [StackOverflow](https://stackoverflow.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/ianzhg/Pokemon/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/ianzhg/Pokemon/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/ianzhg/Pokemon/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/ianzhg/Pokemon/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[MongoDB.com]: https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white
[MongoDB-url]: https://www.mongodb.com/ 
[Express.com]: https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white
[Express-url]: https://expressjs.com/
[Node.js.com]: https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white
[Node.js-url]: https://nodejs.org/en/
[mui.com]: https://img.shields.io/badge/MaterialUI-007FFF?style=for-the-badge&logo=mui&logoColor=white
[mui-url]: https://mui.com
[axios-http.com]: https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white
[axios-http-url]: https://axios-http.com/docs/intro
[getstream-http.com]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[getstream-http-url]: https://getstream.io/
[heroku-http.com]: https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white
[heroku-http-url]: https://www.heroku.com/



