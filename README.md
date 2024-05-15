<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />


<h3 align="center">Jakubski's Dieren</h3>

  <p align="center">
    Een app die mensen opzoek naar een huisdier helpt
    <br />
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Een project die ik gemaakt heb als eindopdracht voor het vak API. Het idee was een soort dating app maar dan voor mensen die opzoek zijn naar een huisdier. Zo kun je een account aanmaken en inloggen. Als de gebruiker ingelogd is kan die dieren zoals honden, katten en overige dieren zoals hamsters en konijnen bekijken en toevoegen aan zijn lijstje met dieren die hij leuk vond.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Vue][Vue.js]][Vue-url]
* [![Fast][Fast.api]][Fast-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>





### Prerequisites
Om te beginnen moet er een virtuele environment worden gemaakt voor python, om de API te laten werken.
```sh
py -m venv myworld
myworld\Scripts\activate.bat
```
Dan alle benodigde pip packages.
```sh
pip install fastapi, uvicorn, pymysql, sqlalchemy,"python-jose[cryptography]" ,"python-jose[cryptography]" 
```
Als alle packages gedownload zijn kun je in het volder van de api gaan en deze command gebruiken om het API op te starten.
```sh
uvicorn index:app --reload
```
om alle endpoints te zien ga je naar deze url:
```sh
http://127.0.0.1:8000/docs
```
Om de Vue project op te starten ga je in de eindopdrachtapi2 folder en gebruik je deze command:
```sh
npm run serve
```


### Installation
Clone the repo
```sh
git clone https://github.com/github_username/repo_name.git
```
3. Install Pip packages
```sh
pip install
```
4. Start de API
```py
uvicorn index:app --reload
```
5. Start de Vue app
```sh
npm run serve
```
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>














<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jakub-chomik/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Fast.api]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[Fast-url]: https://fastapi.tiangolo.com/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
