"""
Exemple usage of the classes Drum, Guitar and Piano
"""
from drum import Drum
from guitar import Guitar
from piano import Piano

if __name__ == '__main__':
    instruments = [Drum(), Guitar(), Piano()]

    for instrument in instruments:
        instrument.play()
