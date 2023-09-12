# STAG-Setup

Příprava pro aplikace, které potřebují přihlášení přes [Ujep STAG](https://portal.ujep.cz/).

* [Fastapi](https://fastapi.tiangolo.com/)
* [Pico.css](https://picocss.com/)

## Deployment

1. Vytvořte soubor **.env** (podle vzoru **.env_example**), včetně proměnné **LOGIN_URL**
2. Změňte **origin_url** parametr na URL stránky, na kterou budete chtít vrátit stagUserTicket
3.  ```
    python app/
    ```

## TODO

* Session
