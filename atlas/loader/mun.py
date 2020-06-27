from typing import List
import csv

class Mun:
    file_path: str
    mun_name: str
    state: str

    def __init__(self, file_path: str) -> None:
        """Constructor for a Municipality object. Municpality objects correspond to a single CSV file in the OpenAddress datasets.

        Arguments:
            file_path {str} -- relative path of the file
        """
        self.file_path = file_path
        parts: List[str] = file_path.split('/')
        self.mun_name = Mun.parse_mun_name(parts.pop(-1))
        self.state = parts.pop(-1).upper()

    def parse_addresses(self) -> List[address]:
        c = csv.reader(open(self.file_path, 'r'))
        index = 0
        ret = list()
        for row in c:
            if index != 0:
                a = address.from_csv(row, self.state, self.mun_name)
                if a.is_valid:
                    ret.append(a)
            index += 1
        return ret

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