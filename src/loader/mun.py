from typing import List

class Mun:
    file_path: str
    mun_name: str

    def __init__(self, file_path: str, mun_name: str) -> None:
        """Constructor for a Municipality object. Municpality objects correspond to a single CSV file in the OpenAddress datasets.

        Arguments:
            file_path {str} -- relative path of the file
            mun_name {str} -- Name of the municipality
        """
        self.file_path = file_path
        self.mun_name = mun_name

    @staticmethod
    def parse_mun_name(raw_name: str) -> str:
        """Clean an OpenAddress filename into a valid, human readable municipality name

        Arguments:
            raw_name {str} -- Raw filename

        Returns:
            str -- Parsed Municipality name
        """
        new_name: str = raw_name.replace('.csv', '')
        n_list: List[str] = new_name.split('_')
        if n_list[0] in ['city', 'town']:
            n_list.pop(0)
            n_list.pop(0)
        index = 0
        for s in n_list:
            n_list[index] = s.capitalize()
            index += 1
        return " ".join(n_list)