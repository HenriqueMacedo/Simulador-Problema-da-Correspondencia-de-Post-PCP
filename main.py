from pcp_simulator import PCPSystem

def main():
    # Instância com solução
    pcp = PCPSystem("Exemplo PCP com Solução")
    pcp.add_piece("b", "ca")
    pcp.add_piece("a", "ab")
    pcp.add_piece("ca", "a")

    pcp.display_system()
    pcp.test_sequence([3, 2, 3, 1])
    pcp.solve_bfs(max_depth=6)

    # Instância sem solução rápida / indefinida
    pcp_sem_solucao = PCPSystem("Exemplo PCP Indecidível")
    pcp_sem_solucao.add_piece("abc", "ab")
    pcp_sem_solucao.add_piece("ca", "a")

    pcp_sem_solucao.display_system()
    pcp_sem_solucao.solve_bfs(max_depth=4)

if __name__ == "__main__":
    main()