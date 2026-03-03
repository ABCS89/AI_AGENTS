create table public.pedido_itens (
    id uuid primary key default uuid_generate_v4(),
    pedido_id uuid references public.pedidos(id) on delete cascade,
    produto_id uuid references public.produtos(id),
    quantidade integer default 1,
    preco_unitario numeric(10,2)
);