import copy

from dados_package import produtos

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in copy.deepcopy(produtos)
]
produtos_ordenados = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'],
    reverse=True
)
produtos_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['preco'],
    reverse=True
)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados, sep='\n')
print()
print(*produtos_preco, sep='\n')
