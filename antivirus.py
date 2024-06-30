import os
import hashlib
import magic
import pyfiglet
import requests

def display_banner():
    banner = pyfiglet.figlet_format("Antivirus")
    print(banner)


def get_file_hashes(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        sha256_hash = hashlib.sha256(file_data).hexdigest()
    return sha256_hash

def identify_file_type(file_path):
    file_type = magic.from_file(file_path)
    return file_type

def check_for_virus_signatures(file_path):
    file_hash = get_file_hashes(file_path)
    virus_signatures = read_file('virus_signatures.json')
    if file_hash in virus_signatures:
        print("File hash is contained in the virus signatures database.")
        return True
    else:
        print("File hash is not contained in the virus signatures database.")
        return False

def update_virus_definitions_from_url():
    try:
        response = requests.get('https://example.com/virus_definitions.txt')
        if response.status_code == 200:
            virus_definitions = response.text.split('\n')
            print("Virus definitions updated successfully.")
            return virus_definitions
        else:
            print("Failed to update virus definitions")
    except requests.exceptions.RequestException as e:
        print("Error updating virus definitions: {}".format(e))

def read_file(file_path):
    """
    Legge il contenuto di un file di testo e lo restituisce.
    
    :param file_path: Il percorso del file da leggere.
    :return: Il contenuto del file come stringa.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("Errore: Il file '{}' non è stato trovato.".format(file_path))
    except IOError:
        print("Errore: Impossibile leggere il file '{}'.".format(file_path))


def update_virus_definitions_from_file():
    file_path = 'virus_definitions.txt'
    content = read_file(file_path)
    if content:
        #print(content)
        print("Virus definitions updated successfully.")


def scan_file(file_path):
    file_type = identify_file_type(file_path)
    print("Scanning file: {} ({})".format(file_path,file_type))
    if check_for_virus_signatures(file_path):
        print("Virus detected in {}!".format(file_path))
    else:
        print("{} is clean.".format(file_path))


def main():
    display_banner()
    update_virus_definitions_from_file()
    while True:
        file_path = input("Enter the file path to scan (or 'q' to quit): ")
        if file_path.lower() == 'q':
            break
        if os.path.isfile(file_path):
            scan_file(file_path)
        else:
            print("Invalid file path: {}".format(file_path))

if __name__ == "__main__":
    main()






