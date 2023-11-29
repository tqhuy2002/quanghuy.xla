from collections import defaultdict
import heapq
from PIL import Image
import io


class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_frequency_table(data):
    frequency = defaultdict(int)
    for symbol in data:
        frequency[symbol] += 1
    return frequency


def build_huffman_tree(freq_table):
    heap = [HuffmanNode(symbol, freq) for symbol, freq in freq_table.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merge = HuffmanNode(None, left.freq + right.freq)
        merge.left = left
        merge.right = right
        heapq.heappush(heap, merge)
    return heap[0]


def build_codewords_table(root):
    codewords = {}

    def generate_codes(current_node, code):
        if current_node.symbol is not None:
            codewords[current_node.symbol] = code
            return
        generate_codes(current_node.left, code + '0')
        generate_codes(current_node.right, code + '1')

    generate_codes(root, '')
    return codewords


def huffman_encoding(data):
    freq_table = build_frequency_table(data)
    huffman_tree = build_huffman_tree(freq_table)
    codewords_table = build_codewords_table(huffman_tree)
    encoded_data = ''.join(codewords_table[symbol] for symbol in data)
    return encoded_data, huffman_tree


def huffman_decoding(encoded_data, tree):
    decoded_data = []
    current_node = tree
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.symbol is not None:
            decoded_data.append(current_node.symbol)
            current_node = tree
    return bytes(decoded_data)


with open('input/huffman_encoding.jpg', 'rb') as file:
    image_data = file.read()

encoded_data, tree = huffman_encoding(image_data)

with open('output/huffman_compressed_image.txt', 'w') as file:
    file.write(encoded_data)

decoded_data = huffman_decoding(encoded_data, tree)

bytes_io = io.BytesIO(decoded_data)
img = Image.open(bytes_io)
img.show()
