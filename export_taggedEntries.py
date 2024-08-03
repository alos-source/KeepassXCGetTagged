import subprocess
import json
import csv

# see reference for keepassxc-cli: https://github.com/keepassxreboot/keepassxc/blob/develop/docs/man/keepassxc-cli.1.adoc

def get_entries_with_tag(database, master_password, tag):
    # Absoluter Pfad zu keepassxc-cli
    keepassxc_cli_path = 'keepassxc-cli'  # Angenommen, keepassxc-cli ist im Systempfad
    
    # Kommando zum Auslesen der Einträge mit dem spezifischen Tag
    command = [
        keepassxc_cli_path, 'search',
        database, tag
    ]
    
    # Ausführung des Kommandos, um alle Einträge mit dem spezifischen Tag zu suchen
    result = subprocess.run(command, input=master_password, text=True, capture_output=True)

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return []

    # Parsen der Ausgabe und Sammeln der Pfade zu den Einträgen
    entries = result.stdout.splitlines()
    tagged_entries = []

    for entry in entries:
        entrypath = entry.strip()
        command_show = [
            keepassxc_cli_path, 'show',
            #'--show-protected',
            database, entrypath
        ]
        result_show = subprocess.run(command_show, input=master_password, text=True, capture_output=True)
        
        if result_show.returncode == 0:
            entry_data = parse_entry(result_show.stdout)
            entry_data['EntryPath'] = entrypath  # Den Pfad des Eintrags hinzufügen
            tagged_entries.append(entry_data)
    
    return tagged_entries

def parse_entry(entry_text):
    entry_data = {}
    lines = entry_text.split('\n')
    for line in lines:
        if ': ' in line:
            key, value = line.split(': ', 1)
            entry_data[key] = value
    return entry_data

def export_to_csv(entries, output_file):
    # Felder für CSV-Datei
    fields = ['EntryPath', 'Title', 'Username', 'Password', 'URL', 'Notes']

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        
        for entry in entries:
            writer.writerow({
                'EntryPath': entry.get('EntryPath', ''),
                'Title': entry.get('Title', ''),
                'Username': entry.get('UserName', ''),
                'Password': entry.get('Password', ''),
                'URL': entry.get('URL', ''),
                'Notes': entry.get('Notes', '')
            })

# example call, might also be the same way with adpoted variables (i.e. path, tag, output) from another script
def main():
    database = r'C:\Pfad\zu\ihrer\Datenbank.kdbx'  # Verwenden Sie einen Rohstring oder ersetzen Sie \ mit \\
    master_password = getpass.getpass(prompt='Master-Passwort eingeben: ')
    tag = 'DigitalLegacy'
    output_file = 'keepassXC_export.csv'

    entries = get_entries_with_tag(database, master_password, tag)
    
    if entries:
        export_to_csv(entries, output_file)
        print(f"Export erfolgreich: {output_file}")
    else:
        print("Keine Einträge gefunden oder Fehler bei der Abfrage.")

if __name__ == "__main__":
    main()
