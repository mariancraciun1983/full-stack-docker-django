<h1 align="center">Fullstack Django</h1>

<div align="center">
  <a href="https://travis-ci.org/mariancraciun1983/full-stack-docker-django">
    <img src="https://secure.travis-ci.org/mariancraciun1983/full-stack-docker-django.svg?branch=master" alt="Travis CI" />
  </a>
  <a href="https://coveralls.io/r/mariancraciun1983/full-stack-docker-django">
    <img src="https://img.shields.io/coveralls/mariancraciun1983/full-stack-docker-django?branch=master&style=flat" alt="Coverage Status" />
  </a>
  <a href="https://pyup.io/account/repos/github/mariancraciun1983/full-stack-docker-django/">
    <img src="https://pyup.io/repos/github/mariancraciun1983/full-stack-docker-django/shield.svg" alt="pyup updates" />
  </a>
  <a href="https://pyup.io/account/repos/github/mariancraciun1983/full-stack-docker-django/">
    <img src="https://pyup.io/repos/github/mariancraciun1983/full-stack-docker-django/python-3-shield.svg" alt="pyup python 3" />
  </a>

  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License" />
  </a>
</div>

This repo is meant to be used as a boilerplate and as part of the [full-stack-docker-compose](https://github.com/mariancraciun1983/full-stack-docker-compose)

TO BE CONTINUED

TODO:
 - [] add periodic_task in the tools task
 - [] add tests
 - [] add api swagger and auth for /cart /auth ?
 - [] fix the docs, structure, 
 - [] linting!


- Push si rollback in productie fara sa trebuiasca sa ma loghez pe serverele de productie. Si trebuie sa nu moara daca e problema de networking. Adica doar initiaza o comanda in productie si aia se ocupa de restul. La Atlas era un post-update hook in git.
- Configurarea unui server de productie cu un script. De exemplu digital ocean iti da optiunea asta, sa il configurezi automat prin comenzi. Daca ai docker nu mai e problema asta, dar la Reflected, cum nu ai docker... Desigur trebuie ceva generic, cel putin pentru ce faci tu acolo.
- uwsgi + nginx = auto configurat setarile. Trebuie sa te gandesti cate workere sunt ideale pentru masina respectiva, setarile de memorile, setarile de upload (gen cate de mare poate sa fie uploadul)
- Auto configurat baza de date, cu aceleasi optimizari necesare pentru productie. La asta si la nginx poti sa copiezi de la Reflected
- Cand faci local nu iti bati capul cu cachingul, ca e mereu local. In productie ai problema: e localhost pe fiecare server, e server separat? Am avut probleme cu django cand era local pe fiecare server, murea siteul la boosturi de traffic, din cauza cacheului, cred ca deadea OOM.
- Cand era cu react si incercam sa vad cum e sa pun in productie, nu prea imi era clar unde e ideal sa hostuiesc fisierele de React, in comparatie cu cele de backend. Tu cred ca stii deja cum  sa faci astea, ca ai proiecte in productie. Dar eu ca noob, nici acum nu imi e clar cum e mai bine. Le pun pe CDN? le servesc de pe aceleasi webserver ca django, instalez un webserver separat pe aceeasi masina.
- La django ai urmatoarea problema in productie: sa zicem ca ai 3 web servers. Nu poti sa pui codul pe toate odata, ca iti pica siteul pentru cateva secunde. Trebuie sa pui treptat: pui pe unu, astepti sa faca python reinterpretarea codului nou, apoi pe celalat si tot asa. Ideal este sa scoti si serverele din rotatie unu cate unu, cat se realizeaza procesul asta.