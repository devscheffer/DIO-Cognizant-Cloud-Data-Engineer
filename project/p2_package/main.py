from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)

from src.create_huffman_algorithm import cls_huffman_algorithm

class huffman_sch:
    def __init__(self,text: str):
        self.text = text
        self.huffman = cls_huffman_algorithm(text)
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text
    def binary_table(self):
        table= self.huffman.mtd_create_binary_table()
        return table
    def frequency_table(self):
        table=self.huffman.mtd_create_frequency_table()
        return table
    def frequency_list(self):
        table=self.huffman.mtd_create_frequency_list()
        return table
    def leaf_path_Preorder(self):
        table=self.huffman.mtd_create_leaf_path_Preorder()
        return table
    def compression(self):
        table=self.huffman.mtd_compression()
        return table

