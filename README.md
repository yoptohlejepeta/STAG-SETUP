# STAG-Setup

Příprava pro aplikace, které potřebují přihlášení přes [Ujep STAG](https://portal.ujep.cz/).

* [Fastapi](https://fastapi.tiangolo.com/)
* [Pico.css](https://picocss.com/)

## Deployment

1. Vytvořte soubor **.env** (podle vzoru **.env_example**), včetně proměnné **APP__LOGIN_URL**
2. Změňte **origin_url** parametr na URL stránky, na kterou budete chtít vrátit stagUserTicket
<<<<<<< HEAD
3.  ```
    python app/
=======
3.
>>>>>>> 3bdc139 (basic redis session)
    ```
    uvicorn app.main:app --reload 
    ```

## Odkazy

* [IS-STAG přihlašování](https://is-stag.zcu.cz/napoveda/web-services/ws_prihlasovani.html)

## TODO

* Dockerfile, Docker-compose
