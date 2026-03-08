# 📌 Antivirus Project

Uno **script Python semplice** per scansionare file alla ricerca di virus basati su **signature hash**. Questo progetto è pensato come esempio didattico o punto di partenza per sviluppare strumenti di sicurezza più avanzati.

---

## 🚀 Caratteristiche

✔️ Interfaccia a riga di comando
✔️ Calcula hash SHA‑256 dei file da analizzare
✔️ Controlla la presenza di firme virali (signature) nel database
✔️ Mostra il tipo di file prima della scansione
✔️ Permette aggiornare le definizioni (placeholder via URL o file locale)

---

## 📦 Requisiti

Assicurati di avere:

* Python 3.6 o superiore
* Le seguenti dipendenze:

```bash
pip install python‑magic pyfiglet requests
```

> Nota: su alcune piattaforme potrebbe essere necessario installare anche il pacchetto di sistema `libmagic` (come `libmagic1` o simili) affinché `python‑magic` funzioni correttamente.

---

## 🧠 Struttura del repository

| File / Cartella         | Descrizione                                         |
| ----------------------- | --------------------------------------------------- |
| `antivirus.py`          | Script principale che esegue la scansione dei file  |
| `virus_signatures.json` | Database delle signature (hash) di virus conosciuti |
| `virus_definitions.txt` | Elenco di firme usate per aggiornamenti locali      |
| `file‑to‑scan/`         | Esempio/file di test da analizzare                  |

---

## ▶️ Come usare

1. **Clona il repository:**

   ```bash
   git clone https://github.com/msabetta/antivirus_project.git
   cd antivirus_project
   ```

2. **Installa le dipendenze:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Esegui lo scanner:**

   ```bash
   python antivirus.py
   ```

4. **Segui le istruzioni:**
   Ti verrà chiesto di inserire il percorso di un file da analizzare. Inserisci il percorso oppure `q` per uscire.

---

## 🛡️ Come funziona

Lo script:

1. Calcola l’hash SHA‑256 del file da analizzare.
2. Confronta l’hash con le firme presenti in `virus_signatures.json`.
3. Segnala se il file è “pulito” o presente nel database delle virus signature.

---

## 📌 Aggiornamento delle definizioni

Sono presenti due funzioni di aggiornamento:

* **Da file locale** (`virus_definitions.txt`)
* **Da URL remoto** (demo placeholder), che puoi personalizzare

> Nota: al momento la funzione remota usa un URL di esempio e va adattata per un servizio reale.

---

## 📈 Miglioramenti futuri

💡 Alcune idee per estendere il progetto:

* Aggiungere **scansione ricorsiva di directory**
* Integrare **servizi di threat intelligence**
* Aggiungere aggiornamenti automatici delle signature
* Implementare un’interfaccia grafica o web

---

## 📄 Licenza

Questo progetto è **open‑source**. Assicurati di attribuire correttamente qualsiasi uso o modifica.


## 📚 Riferimenti

* https://medium.com/@Scofield_Idehen/build-an-antivirus-with-python-beginners-guide-a9591448af05

