# Lernplan für Python-Anfänger: `uv` und `git`

Dieser 4-wöchentliche Lernplan führt Python-Anfänger in die Verwendung von `uv` (ein moderner Python-Paket- und Projektmanager) und `git` (Versionskontrolle) ein. Er richtet sich an Lernende mit grundlegenden Python-Kenntnissen (z. B. Variablen, Schleifen, Funktionen) und ist sowohl für Linux- als auch Windows-Nutzer geeignet. Der Plan kombiniert Theorie, praktische Übungen und ein Abschlussprojekt, um moderne Python-Workflows zu vermitteln.

## Voraussetzungen
- Python 3.8 oder höher installiert ([python.org](https://www.python.org/downloads/)).
- Grundlegende Kenntnisse der Kommandozeile (z. B. `cd`, `ls`/`dir`).
- Ein Texteditor (z. B. VS Code, PyCharm, oder Notepad++).
- Internetzugang für Installationen und Tutorials.

## Woche 1: Grundlagen und Installation
**Ziel**: Verstehe `uv` und `git`, installiere sie und lerne grundlegende Befehle.

### Tag 1: Einführung in `uv` und `git`
- **Lernziele**:
  - Verstehe, was `uv` (Paket- und Projektmanagement) und `git` (Versionskontrolle) sind.
  - Lerne, warum virtuelle Umgebungen und Versionskontrolle wichtig sind.
- **Aufgaben**:
  - Lies die Einführung zu `uv` auf [docs.astral.sh/uv](https://docs.astral.sh/uv).
  - Lies die Einführung zu `git` auf [git-scm.com/doc](https://git-scm.com/doc).
  - Notiere: Warum sind isolierte Umgebungen (z. B. mit `uv`) und Versionskontrolle (z. B. mit `git`) für Python-Projekte nützlich?

### Tag 2: Installation von `uv` und `git`
- **Lernziele**:
  - Installiere `uv` und `git` benutzerbasiert.
  - Überprüfe die Installationen.
- **Aufgaben**:
  - **Linux**:
    - Installiere `git`:
      ```bash
      sudo apt install git  # Ubuntu/Debian
      sudo dnf install git  # Fedora
      ```
    - Installiere `uv`:
      ```bash
      curl -LsSf https://astral.sh/uv/install.sh | sh
      ```
    - Füge `~/.local/bin` zu `PATH` hinzu:
      ```bash
      echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc
      ```
  - **Windows**:
    - Installiere `git` von [git-scm.com](https://git-scm.com/download/win) (wähle Standardoptionen).
    - Installiere `uv` in PowerShell:
      ```powershell
      Invoke-RestMethod -Uri https://astral.sh/uv/install.ps1 | Invoke-Expression
      ```
    - Füge den `uv`-Pfad (z. B. `C:\Users\<DeinBenutzer>\AppData\Local\Programs\uv`) zu `PATH` hinzu:
      - Öffne Systemeinstellungen → Erweiterte Systemeinstellungen → Umgebungsvariablen → `Path` bearbeiten.
  - Überprüfe Installationen:
    ```bash
    git --version
    uv --version
    ```

### Tag 3: Grundlegende `git`-Befehle
- **Lernziele**:
  - Initialisiere ein Git-Repository und mache erste Commits.
- **Aufgaben**:
  - Erstelle ein Verzeichnis und initialisiere ein Repository:
    ```bash
    mkdir mein_projekt
    cd mein_projekt
    git init
    ```
  - Erstelle eine `README.md`-Datei:
    ```markdown
    # Mein erstes Projekt
    Dies ist ein Testprojekt.
    ```
  - Füge die Datei hinzu und committe:
    ```bash
    git add README.md
    git commit -m "Initial commit"
    ```
  - Überprüfe den Status:
    ```bash
    git status
    ```

### Tag 4: Grundlegende `uv`-Befehle
- **Lernziele**:
  - Erstelle ein Projekt mit `uv` und verstehe virtuelle Umgebungen.
- **Aufgaben**:
  - Erstelle ein neues Projekt mit `uv`:
    ```bash
    uv init mein_projekt --git
    cd mein_projekt
    ```
  - Untersuche die generierte Struktur (`pyproject.toml`, `.python-version`, `README.md`).
  - Erstelle eine virtuelle Umgebung:
    ```bash
    uv venv
    ```
  - Führe ein einfaches Skript aus:
    ```bash
    echo "print('Hallo uv!')" > main.py
    uv run python main.py
    ```
  - Committe die Änderungen:
    ```bash
    git add .
    git commit -m "Projekt mit uv initialisiert"
    ```

### Tag 5: Wiederholung und Reflexion
- **Aufgaben**:
  - Wiederhole die Befehle: `git init`, `git add`, `git commit`, `uv init`, `uv venv`, `uv run`.
  - Schreibe eine kurze Notiz: Was hast du über `uv` und `git` gelernt? Welche Befehle fühlten sich intuitiv an?

## Woche 2: Abhängigkeiten und Projektstruktur
**Ziel**: Lerne, Abhängigkeiten mit `uv` zu verwalten und `git` für Projektänderungen zu nutzen.

### Tag 1: Abhängigkeiten mit `uv` hinzufügen
- **Lernziele**:
  - Installiere Python-Pakete und verstehe `pyproject.toml`.
- **Aufgaben**:
  - Füge die `requests`-Bibliothek hinzu:
    ```bash
    uv add requests
    ```
  - Untersuche `pyproject.toml` und `uv.lock` (wurde automatisch erstellt).
  - Führe ein Skript aus, das `requests` nutzt:
    ```python
    # main.py
    import requests
    response = requests.get("https://api.github.com")
    print(response.status_code)
    ```
    ```bash
    uv run python main.py
    ```
  - Committe die Änderungen:
    ```bash
    git add .
    git commit -m "requests hinzugefügt und Beispielskript erstellt"
    ```

### Tag 2: Virtuelle Umgebungen synchronisieren
- **Lernziele**:
  - Verstehe, wie `uv` Umgebungen mit `uv.lock` synchronisiert.
- **Aufgaben**:
  - Synchronisiere die Umgebung:
    ```bash
    uv sync
    ```
  - Teste, ob `requests` korrekt installiert ist:
    ```bash
    uv run python -c "import requests; print(requests.__version__)"
    ```
  - Erstelle eine `.gitignore`-Datei, um die virtuelle Umgebung auszuschließen:
    ```gitignore
    .venv/
    __pycache__/
    ```
  - Committe:
    ```bash
    git add .gitignore
    git commit -m "gitignore hinzugefügt"
    ```

### Tag 3: Arbeiten mit `git branch`
- **Lernziele**:
  - Lerne, wie man Branches in `git` erstellt und verwendet.
- **Aufgaben**:
  - Erstelle einen neuen Branch:
    ```bash
    git branch feature
    git checkout feature
    ```
  - Ändere `main.py`, um einen neuen Endpunkt zu nutzen:
    ```python
    # main.py
    import requests
    response = requests.get("https://api.github.com/users/octocat")
    print(response.json()["login"])
    ```
  - Committe die Änderung:
    ```bash
    git add main.py
    git commit -m "Neuer API-Endpunkt hinzugefügt"
    ```
  - Wechsle zurück zum `main`-Branch:
    ```bash
    git checkout main
    ```

### Tag 4: Mergen mit `git`
- **Lernziele**:
  - Lerne, wie man Branches merged.
- **Aufgaben**:
  - Merge den `feature`-Branch in `main`:
    ```bash
    git merge feature
    ```
  - Überprüfe das Ergebnis:
    ```bash
    git log --oneline
    ```
  - Lösche den `feature`-Branch:
    ```bash
    git branch -d feature
    ```
  - Führe das aktualisierte Skript aus:
    ```bash
    uv run python main.py
    ```

### Tag 5: Wiederholung und Reflexion
- **Aufgaben**:
  - Wiederhole: `uv add`, `uv sync`, `git branch`, `git merge`.
  - Schreibe: Wie hilft `uv` bei der Verwaltung von Abhängigkeiten? Wie unterstützt `git` die Organisation von Code-Änderungen?

## Woche 3: Tests und Entwickler-Tools
**Ziel**: Integriere Tests und Entwickler-Tools mit `uv` und nutze `git` für fortgeschrittene Workflows.

### Tag 1: Tests mit `pytest`
- **Lernziele**:
  - Installiere und nutze `pytest` für Tests.
- **Aufgaben**:
  - Füge `pytest` als Entwickler-Abhängigkeit hinzu:
    ```bash
    uv add --dev pytest
    ```
  - Erstelle eine Testdatei:
    ```python
    # test_main.py
    def test_example():
        assert 1 + 1 == 2
    ```
  - Führe Tests aus:
    ```bash
    uv run pytest
    ```
  - Committe:
    ```bash
    git add test_main.py
    git commit -m "pytest hinzugefügt und erster Test erstellt"
    ```

### Tag 2: Code-Formatierung mit `black`
- **Lernziele**:
  - Nutze `black` für automatische Code-Formatierung.
- **Aufgaben**:
  - Füge `black` hinzu:
    ```bash
    uv add --dev black
    ```
  - Formatiere den Code:
    ```bash
    uv run black .
    ```
  - Committe die Änderungen:
    ```bash
    git add .
    git commit -m "Code mit black formatiert"
    ```

### Tag 3: Arbeiten mit Remote-Repositories
- **Lernziele**:
  - Verbinde ein lokales Repository mit GitHub.
- **Aufgaben**:
  - Erstelle ein neues Repository auf [github.com](https://github.com).
  - Verbinde das lokale Repository:
    ```bash
    git remote add origin <dein-repository-URL>
    ```
  - Pushe die Änderungen:
    ```bash
    git push -u origin main
    ```
  - Überprüfe das Repository auf GitHub.

### Tag 4: Kollaboration mit `git`
- **Lernziele**:
  - Lerne, wie man Pull Requests erstellt.
- **Aufgaben**:
  - Erstelle einen neuen Branch:
    ```bash
    git checkout -b feature-test
    ```
  - Ändere `test_main.py`:
    ```python
    def test_another():
        assert 2 * 2 == 4
    ```
  - Committe und pushe:
    ```bash
    git add test_main.py
    git commit -m "Neuer Test hinzugefügt"
    git push origin feature-test
    ```
  - Erstelle einen Pull Request auf GitHub und merge ihn.

### Tag 5: Wiederholung und Reflexion
- **Aufgaben**:
  - Wiederhole: `uv add --dev`, `uv run pytest`, `git push`, `git remote`.
  - Schreibe: Wie haben `pytest` und `black` deinen Workflow verbessert? Wie hilft GitHub bei der Zusammenarbeit?

## Woche 4: Abschlussprojekt
**Ziel**: Erstelle ein kleines Python-Projekt mit `uv` und `git`, inklusive Tests und Remote-Repository.

### Tag 1-2: Projektplanung
- **Lernziele**:
  - Entwerfe ein kleines Projekt (z. B. ein CLI-Tool zum Abrufen von Wetterdaten).
- **Aufgaben**:
  - Wähle ein Projekt: Ein CLI-Tool, das Wetterdaten von einer API (z. B. [openweathermap.org](https://openweathermap.org)) abruft.
  - Erstelle ein neues Projekt:
    ```bash
    uv init wetter_app --app --git
    cd wetter_app
    ```
  - Füge Abhängigkeiten hinzu:
    ```bash
    uv add requests click
    ```

### Tag 3-4: Projektentwicklung
- **Lernziele**:
  - Implementiere das Projekt und nutze `git` für Versionskontrolle.
- **Aufgaben**:
  - Erstelle das Hauptprogramm:
    ```python
    # main.py
    import click
    import requests

    @click.command()
    @click.argument("city")
    def get_weather(city):
        api_key = "dein-api-schlüssel"  # Von openweathermap.org
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temp = data["main"]["temp"]
            click.echo(f"Temperatur in {city}: {temp}°C")
        else:
            click.echo("Fehler beim Abrufen der Daten.")

    if __name__ == "__main__":
        get_weather()
    ```
  - Erstelle Tests:
    ```python
    # test_main.py
    def test_placeholder():
        assert True
    ```
  - Committe regelmäßig:
    ```bash
    git add .
    git commit -m "Wetter-CLI implementiert"
    ```

### Tag 5: Fertigstellung und Veröffentlichung
- **Lernziele**:
  - Teste das Projekt, pushe es nach GitHub und dokumentiere es.
- **Aufgaben**:
  - Führe Tests aus:
    ```bash
    uv run pytest
    ```
  - Formatiere den Code:
    ```bash
    uv run black .
    ```
  - Aktualisiere `README.md`:
    ```markdown
    # Wetter-CLI
    Ein Kommandozeilen-Tool zum Abrufen von Wetterdaten.

    ## Installation
    ```bash
    uv pip install .
    ```

    ## Nutzung
    ```bash
    uv run wetter_app Berlin
    ```
    ```
  - Pushe das Projekt nach GitHub:
    ```bash
    git remote add origin <dein-repository-URL>
    git push -u origin main
    ```
  - Schreibe eine kurze Reflexion: Was hast du gelernt? Was war herausfordernd?

## Ressourcen
- `uv`-Dokumentation: [docs.astral.sh/uv](https://docs.astral.sh/uv)
- `git`-Dokumentation: [git-scm.com/doc](https://git-scm.com/doc)
- Python-Tutorials: [python.org](https://www.python.org/about/gettingstarted/)
- GitHub-Leitfaden: [guides.github.com](https://guides.github.com)

## Nächste Schritte
- Vertiefe deine Kenntnisse in `uv` mit fortgeschrittenen Features (z. B. `uv build` für PyPI-Pakete).
- Lerne weitere `git`-Befehle (z. B. `git rebase`, `git stash`).
- Erkunde andere Python-Tools wie `poetry` oder `ruff`.