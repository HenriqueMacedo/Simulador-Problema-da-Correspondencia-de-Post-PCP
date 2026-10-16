"""
SIMULADOR DO PROBLEMA DA CORRESPONDÊNCIA DE POST (PCP).
Referência: Diverio & Menezes (2011), Cap. 9 - Computabilidade.
Para o seminário de Teoria da Computação.
"""

from collections import deque
from typing import List, Tuple, Optional


class PCPPiece:
    """Representa uma peça (dominó) do PCP contendo CIMA (top) e BAIXO (bottom)."""

    def __init__(self, index: int, top: str, bottom: str):
        self.index = index
        self.top = top
        self.bottom = bottom

    def __repr__(self) -> str:
        return f"Peça {self.index} [{self.top} / {self.bottom}]"


class PCPSystem:
    """Implementa o Sistema de Post S = {(x_1, y_1), ..., (x_n, y_n)}."""

    def __init__(self, name: str = "Instância PCP"):
        self.name = name
        self.pieces: List[PCPPiece] = []

    def add_piece(self, top: str, bottom: str) -> None:
        """Cadastra uma nova peça no sistema."""
        idx = len(self.pieces) + 1
        self.pieces.append(PCPPiece(idx, top, bottom))

    def get_piece(self, index: int) -> Optional[PCPPiece]:
        if 1 <= index <= len(self.pieces):
            return self.pieces[index - 1]
        return None

    def display_system(self) -> None:
        """Exibe as peças cadastradas no terminal."""
        print(f"\n==================== {self.name} ====================")
        print(f"Total de peças: {len(self.pieces)}")
        for p in self.pieces:
            print(f"  (Peça {p.index}) -> CIMA: '{p.top}' | BAIXO: '{p.bottom}'")
        print("=========================================================\n")

    def test_sequence(self, sequence: List[int]) -> bool:
        """
        Recebe uma sequência de índices, concatena as partes de CIMA e BAIXO
        e realiza a comparação automática detalhada.
        """
        if not sequence:
            print("Erro: A sequência de índices não pode ser vazia.")
            return False

        top_str = ""
        bottom_str = ""

        for idx in sequence:
            piece = self.get_piece(idx)
            if not piece:
                print(f"Erro: Peça com índice {idx} não existe.")
                return False
            top_str += piece.top
            bottom_str += piece.bottom

        is_match = top_str == bottom_str
        print(f"Sequência testada: {sequence}")
        print(f"  CIMA  : '{top_str}'")
        print(f"  BAIXO : '{bottom_str}'")
        print(f"  Resultado: {'Solução válida!' if is_match else 'Não é solução'}")
        return is_match

    def solve_bfs(self, max_depth: int = 5) -> Optional[List[int]]:
        """
        Busca uma solução para o PCP usando BFS até uma profundidade máxima.
        """
        queue = deque([([], "", "")])

        while queue:
            seq, top, bottom = queue.popleft()

            if len(seq) > max_depth:
                continue

            if seq and top == bottom:
                print(f"Solução encontrada via BFS (profundidade {len(seq)}): {seq}")
                return seq

            for piece in self.pieces:
                new_seq = seq + [piece.index]
                new_top = top + piece.top
                new_bottom = bottom + piece.bottom

                # Otimização: só continua se um for prefixo do outro
                if new_top.startswith(new_bottom) or new_bottom.startswith(new_top):
                    queue.append((new_seq, new_top, new_bottom))

        print(f"Nenhuma solução encontrada até a profundidade máxima de {max_depth}.")
        return None